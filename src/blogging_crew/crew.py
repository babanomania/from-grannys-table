from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from blogging_crew.tools.custom_tool import ImageSearchTool

@CrewBase
class BloggingCrew():
    """BloggingCrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True
        )

    @agent
    def grandmother(self) -> Agent:
        return Agent(
            config=self.agents_config['grandmother'],
            verbose=True
        )

    @agent
    def granddaughter(self) -> Agent:
        return Agent(
            config=self.agents_config['granddaughter'],
            tools=[ImageSearchTool()],
            verbose=True
        )

    @task
    def research_task(self) -> Task:
        return Task(
            config=self.tasks_config['research_task'],
            agent=self.researcher()
        )

    @task
    def outline_task(self) -> Task:
        return Task(
            config=self.tasks_config['outline_task'],
            agent=self.grandmother()
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            config=self.tasks_config['writing_task'],
            agent=self.grandmother()
        )

    @task
    def enhancement_task(self) -> Task:
        return Task(
            config=self.tasks_config['enhancement_task'],
            agent=self.granddaughter(),
            output_file='output.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BloggingCrew crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical,
        )
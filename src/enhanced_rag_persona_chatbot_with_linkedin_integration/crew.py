import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	ScrapegraphScrapeTool
)





@CrewBase
class EnhancedRagPersonaChatbotWithLinkedinIntegrationCrew:
    """EnhancedRagPersonaChatbotWithLinkedinIntegration crew"""

    
    @agent
    def document_knowledge_manager(self) -> Agent:
        
        return Agent(
            config=self.agents_config["document_knowledge_manager"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def persona_chatbot(self) -> Agent:
        
        return Agent(
            config=self.agents_config["persona_chatbot"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def linkedin_profile_scraper(self) -> Agent:
        
        return Agent(
            config=self.agents_config["linkedin_profile_scraper"],
            
            
            tools=[
				ScrapegraphScrapeTool()
            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def scrape_linkedin_profile_data(self) -> Task:
        return Task(
            config=self.tasks_config["scrape_linkedin_profile_data"],
            markdown=False,
        )
    
    @task
    def process_persona_data(self) -> Task:
        return Task(
            config=self.tasks_config["process_persona_data"],
            markdown=False,
        )
    
    @task
    def answer_user_question(self) -> Task:
        return Task(
            config=self.tasks_config["answer_user_question"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the EnhancedRagPersonaChatbotWithLinkedinIntegration crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )

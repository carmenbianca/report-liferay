import gantt
from datetime import date, timedelta

WORKSHOP = "#55CDFC"
DEADLINE = "#F7A8B8"
DRAFT = "#DDDDDD"

plan_de_campagne = gantt.Project("Plan de campagne", color="#FF0018")

plan_de_campagne_tasks = [
    gantt.Task("Write plan de campagne", start=date(2020, 2, 3), duration=5*5),
    gantt.Task("Revise plan de campagne", start=date(2020, 3, 10), duration=5*2-1),
    gantt.Task("First draft plan de campagne", start=date(2020, 2, 28), duration=1, color=DRAFT),
    gantt.Task("Deadline plan de campagne", start=date(2020, 3, 9), duration=1, color=DEADLINE),
    gantt.Task("Second deadline plan de campagne", start=date(2020, 3, 23), duration=1, color=DEADLINE),
    gantt.Task("Workshop plan de campagne", start=date(2020, 2, 11), duration=1, color=WORKSHOP),
]

for task in plan_de_campagne_tasks:
    plan_de_campagne.add_task(task)

research = gantt.Project("Research", color="#FFA52C")

research_tasks = [
    gantt.Task("Preliminary research", start=date(2020, 2, 3), duration=5*5),
    gantt.Task("Research sub-question 1", start=date(2020, 3, 2), duration=3),
    gantt.Task("Research sub-question 2", start=date(2020, 3, 5), duration=3),
    gantt.Task("Research sub-question 3", start=date(2020, 3, 10), duration=3),
    gantt.Task("Research sub-question 4", start=date(2020, 3, 13), duration=3),
    gantt.Task("Research sub-question 5", start=date(2020, 3, 18), duration=3),
    gantt.Task("Put it all together", start=date(2020, 3, 23), duration=5),
    gantt.Task("Workshop concluding and analysing", start=date(2020, 3, 24), duration=1, color=WORKSHOP),
    gantt.Task("Legal and Licensing Workshop", start=date(2020, 4, 15), duration=3),
]

for task in research_tasks:
    research.add_task(task)

sync = gantt.Project("Synchronisation", color="#FFFF41")

sync_tasks = [
    gantt.Task("Synchronise with Matija", start=the_date, duration=1) for the_date in (date(2020, 2, 18) + timedelta(i) for i in (x*14 for x in range(9)))
]
sync_tasks += [
    gantt.Task("On-location meeting with Matija and Martin", start=date(2020, 4, 6), duration=1),
    gantt.Task("Product retrospective", start=date(2020, 5, 26), duration=1),
]

for task in sync_tasks:
    sync.add_task(task)

implementation = gantt.Project("Implementation", color="#008018")

implementation_tasks = [
    gantt.Task("Create requirements analysis", start=date(2020, 3, 30), duration=3),
    gantt.Task("Familiarise with tools", start=date(2020, 3, 30), duration=5),
    gantt.Task("Implementation", start=date(2020, 4, 6), duration=5*9),
    gantt.Task("Hand over proof-of-concept", start=date(2020, 6, 5), duration=1),
]

for task in implementation_tasks:
    implementation.add_task(task)

reporting = gantt.Project("Reporting", color="#3333f9")

reporting_tasks = [
    gantt.Task("Convert plan de campagne to report", start=date(2020, 3, 2), duration=2),
    gantt.Task("Continuous reporting", start=date(2020, 3, 2), duration=5*13),
    gantt.Task("Wrap up report", start=date(2020, 6, 1), duration=5*3),
    gantt.Task("Workshop reporting", start=date(2020, 5, 4), duration=1, color=WORKSHOP),
    gantt.Task("First draft report", start=date(2020, 5, 25), duration=1, color=DRAFT),
    gantt.Task("Deadline report", start=date(2020, 6, 19), duration=1, color=DEADLINE),
]

for task in reporting_tasks:
    reporting.add_task(task)

presentation = gantt.Project("Presentation", color="#86007D")

presentation_tasks = [
    gantt.Task("Make presentation", start=date(2020, 6, 22), duration=5*2),
    gantt.Task("Presentation in Leeuwarden", start=date(2020, 7, 6), duration=3, color="#FF0000"),
]

for task in presentation_tasks:
    presentation.add_task(task)

project = gantt.Project("Automated Copyright And Licensing Compliance")

project.add_task(plan_de_campagne)
project.add_task(research)
project.add_task(sync)
project.add_task(implementation)
project.add_task(reporting)
project.add_task(presentation)

project.make_svg_for_tasks(
    filename='gantt.svg',
    start=date(2020, 2, 1),
    end=date(2020, 7, 17),
    scale=gantt.DRAW_WITH_WEEKLY_SCALE,
)

project.make_svg_for_tasks(
    filename='gantt-full.svg',
    start=date(2020, 2, 1),
    end=date(2020, 7, 17),
)
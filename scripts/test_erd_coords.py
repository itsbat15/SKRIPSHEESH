"""
Test script to compute new neat aligned coordinates for ARTHA ERD
"""

# Let's define the 4 main column center X's:
COL_A = 240   # users, daily_reconciliations
COL_B = 620   # branches, students
COL_C = 1060  # study_groups, enrollments, tuition_bills
COL_D = 1520  # course_packages, payments, payment_proofs

# Midpoints:
MID_AB = (COL_A + COL_B) // 2  # 430
MID_BC = (COL_B + COL_C) // 2  # 840 (Mengelola, Mengambil)
MID_CD = (COL_C + COL_D) // 2  # 1290 (Ditawarkan, Diselesaikan)

# Rows (Y centers):
ROW_1 = 180   # branches, study_groups, course_packages
ROW_R1 = 300  # rel_memiliki, rel_menaungi, rel_ditempati, rel_ditawarkan
ROW_2 = 420   # users, students, enrollments
ROW_R2 = 540  # rel_melakukan, rel_menerbitkan, rel_melayani
ROW_3 = 660   # daily_reconciliations, tuition_bills, payments
ROW_R3 = 780  # rel_melampirkan
ROW_4 = 900   # payment_proofs, rel_memvalidasi

# Entity dimensions:
ENT_W = 140
ENT_H = 45

# Relationship dimensions:
REL_W = 110
REL_H = 50

entities = {
    'ent_branches':        {'cx': COL_B, 'cy': ROW_1, 'w': 140, 'h': 45, 'name': 'branches'},
    'ent_study_groups':    {'cx': COL_C, 'cy': ROW_1, 'w': 140, 'h': 45, 'name': 'study_groups'},
    'ent_course_packages': {'cx': COL_D, 'cy': ROW_1, 'w': 150, 'h': 45, 'name': 'course_packages'},
    'ent_users':           {'cx': COL_A, 'cy': ROW_2, 'w': 140, 'h': 45, 'name': 'users'},
    'ent_students':        {'cx': COL_B, 'cy': ROW_2, 'w': 140, 'h': 45, 'name': 'students'},
    'ent_enrollments':     {'cx': COL_C, 'cy': ROW_2, 'w': 140, 'h': 45, 'name': 'enrollments'},
    'ent_daily_rec':       {'cx': COL_A, 'cy': ROW_3, 'w': 170, 'h': 45, 'name': 'daily_reconciliations'},
    'ent_tuition_bills':   {'cx': COL_C, 'cy': ROW_3, 'w': 140, 'h': 45, 'name': 'tuition_bills'},
    'ent_payments':        {'cx': COL_D, 'cy': ROW_3, 'w': 140, 'h': 45, 'name': 'payments'},
    'ent_payment_proofs':  {'cx': COL_D, 'cy': ROW_4, 'w': 150, 'h': 45, 'name': 'payment_proofs'},
}

relations = {
    # Row 1 horizontal:
    'rel_mengelola':    {'cx': MID_BC, 'cy': ROW_1, 'w': 110, 'h': 50, 'name': 'Mengelola'},
    # Between Row 1 and Row 2:
    'rel_memiliki':     {'cx': COL_A,  'cy': ROW_R1, 'w': 110, 'h': 50, 'name': 'Memiliki'},
    'rel_menaungi':     {'cx': COL_B,  'cy': ROW_R1, 'w': 110, 'h': 50, 'name': 'Menaungi'},
    'rel_ditempati':    {'cx': COL_C,  'cy': ROW_R1, 'w': 110, 'h': 50, 'name': 'Ditempati'},
    'rel_ditawarkan':   {'cx': MID_CD, 'cy': ROW_R1, 'w': 110, 'h': 50, 'name': 'Ditawarkan'},
    # Row 2 horizontal:
    'rel_mengambil':    {'cx': MID_BC, 'cy': ROW_2, 'w': 110, 'h': 50, 'name': 'Mengambil'},
    # Between Row 2 and Row 3:
    'rel_melakukan':    {'cx': COL_A,  'cy': ROW_R2, 'w': 110, 'h': 50, 'name': 'Melakukan'},
    'rel_menerbitkan':  {'cx': COL_C,  'cy': ROW_R2, 'w': 115, 'h': 50, 'name': 'Menerbitkan'},
    'rel_melayani':     {'cx': MID_CD, 'cy': ROW_R2, 'w': 110, 'h': 50, 'name': 'Melayani'},
    # Row 3 horizontal:
    'rel_diselesaikan': {'cx': MID_CD, 'cy': ROW_3, 'w': 115, 'h': 50, 'name': 'Diselesaikan'},
    # Between Row 3 and Row 4:
    'rel_melampirkan':  {'cx': COL_D,  'cy': ROW_R3, 'w': 115, 'h': 50, 'name': 'Melampirkan'},
    # Bottom / Perimeter:
    'rel_memvalidasi':  {'cx': 1200,   'cy': ROW_4,  'w': 110, 'h': 50, 'name': 'Memvalidasi'},
    'rel_mengadakan':   {'cx': 80,     'cy': 420,    'w': 110, 'h': 50, 'name': 'Mengadakan'},
    'rel_menerima':     {'cx': 1750,   'cy': 420,    'w': 110, 'h': 50, 'name': 'Menerima'},
}

print("Node layout generated successfully.")


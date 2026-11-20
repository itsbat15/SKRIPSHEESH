"""
build_tidy_erd.py
=================
Generates a perfectly aligned, symmetrical, orthogonal ERD for ARTHA (Peter Chen notation)
without attributes, strictly following Pak Arif's feedback.
All vertical connections: dx = 0 (100% straight).
All horizontal connections: dy = 0 (100% straight).
Symmetric diagonal connections: slopes match 100%.
"""

import xml.etree.ElementTree as ET
import subprocess
import os

# ----------------- COORDINATE DEFINITIONS -----------------
# 4 Main Columns:
COL_A = 240   # users, daily_reconciliations
COL_B = 620   # branches, students
COL_C = 1060  # study_groups, enrollments, tuition_bills
COL_D = 1520  # course_packages, payments, payment_proofs

# Midpoint Columns:
MID_AB = (COL_A + COL_B) // 2  # 430  (rel_memiliki)
MID_BC = (COL_B + COL_C) // 2  # 840  (rel_mengelola, rel_mengambil)
MID_CD = (COL_C + COL_D) // 2  # 1290 (rel_ditawarkan, rel_diselesaikan)

# Rows (Y centers):
ROW_1 = 180   # branches, study_groups, course_packages
ROW_R1 = 300  # rel_memiliki, rel_menaungi, rel_ditempati, rel_ditawarkan
ROW_2 = 420   # users, students, enrollments
ROW_R2 = 540  # rel_melakukan, rel_menerbitkan
ROW_3 = 660   # daily_reconciliations, tuition_bills, payments
ROW_R3 = 780  # rel_melampirkan
ROW_4 = 900   # payment_proofs

# Perimeter & Special Relationships:
X_PERIM_L = 90   # rel_mengadakan
X_PERIM_R = 1710 # rel_menerima
Y_BUS_TOP = 95   # top bus for branches -> menerima & mengadakan
Y_BUS_MID = 540  # middle bus for users -> melayani
Y_BUS_BOT = 900  # bottom bus for users -> memvalidasi

# Entity specifications: id, name, cx, cy, w, h
ENTITIES = [
    ('ent_branches',        'branches',             COL_B, ROW_1, 140, 45),
    ('ent_study_groups',    'study_groups',         COL_C, ROW_1, 140, 45),
    ('ent_course_packages', 'course_packages',      COL_D, ROW_1, 150, 45),
    ('ent_users',           'users',                COL_A, ROW_2, 140, 45),
    ('ent_students',        'students',             COL_B, ROW_2, 140, 45),
    ('ent_enrollments',     'enrollments',          COL_C, ROW_2, 140, 45),
    ('ent_daily_rec',       'daily_reconciliations',COL_A, ROW_3, 170, 45),
    ('ent_tuition_bills',   'tuition_bills',        COL_C, ROW_3, 140, 45),
    ('ent_payments',        'payments',             COL_D, ROW_3, 140, 45),
    ('ent_payment_proofs',  'payment_proofs',       COL_D, ROW_4, 150, 45),
]

# Relationship specifications: id, name, cx, cy, w, h
RELATIONSHIPS = [
    # Top horizontal:
    ('rel_mengelola',    'Mengelola',    MID_BC,    ROW_1,  110, 50),
    # Tier 1-2:
    ('rel_memiliki',     'Memiliki',     MID_AB,    ROW_R1, 110, 50),
    ('rel_menaungi',     'Menaungi',     COL_B,     ROW_R1, 110, 50),
    ('rel_ditempati',    'Ditempati',    COL_C,     ROW_R1, 110, 50),
    ('rel_ditawarkan',   'Ditawarkan',   MID_CD,    ROW_R1, 110, 50),
    # Mid horizontal:
    ('rel_mengambil',    'Mengambil',    MID_BC,    ROW_2,  110, 50),
    # Tier 2-3:
    ('rel_melakukan',    'Melakukan',    COL_A,     ROW_R2, 110, 50),
    ('rel_menerbitkan',  'Menerbitkan',  COL_C,     ROW_R2, 115, 50),
    ('rel_melayani',     'Melayani',     1360,      ROW_R2, 110, 50),
    # Tier 3 horizontal:
    ('rel_diselesaikan', 'Diselesaikan', MID_CD,    ROW_3,  115, 50),
    # Tier 3-4:
    ('rel_melampirkan',  'Melampirkan',  COL_D,     ROW_R3, 115, 50),
    # Special & Perimeter:
    ('rel_memvalidasi',  'Memvalidasi',  1220,      ROW_4,  110, 50),
    ('rel_mengadakan',   'Mengadakan',   X_PERIM_L, 420,    110, 50),
    ('rel_menerima',     'Menerima',     X_PERIM_R, 420,    110, 50),
]

print("Specification loaded.")


"use client";

import { createContext, useContext, useMemo, useState } from "react";
import {
  bills as initialBills,
  classEnrollments as initialClassEnrollments,
  classes as initialClasses,
  payments as initialPayments,
  pengeluaranData as initialPengeluaran,
  students as initialStudents,
} from "@/data/mockFrontdeskData";

const FrontdeskDataContext = createContext(null);

const today = () => new Date().toISOString().slice(0, 10);
const nextId = (items) => Math.max(0, ...items.map((item) => Number(item.id) || 0)) + 1;

export function FrontdeskDataProvider({ children }) {
  const [students, setStudents] = useState(initialStudents);
  const [classRecords, setClassRecords] = useState(initialClasses);
  const [classEnrollments, setClassEnrollments] = useState(initialClassEnrollments);
  const [bills, setBills] = useState(initialBills);
  const [payments, setPayments] = useState(initialPayments);
  const [pengeluaran, setPengeluaran] = useState(initialPengeluaran);

  const classes = useMemo(
    () =>
      classRecords.map((kelas) => ({
        ...kelas,
        current_students: classEnrollments.filter(
          (enrollment) =>
            enrollment.class_id === kelas.id &&
            enrollment.enrollment_status === "active"
        ).length,
      })),
    [classRecords, classEnrollments]
  );

  const recordPaymentForBill = (bill, { method, notes } = {}) => {
    const paymentDate = today();
    const payment = {
      id: nextId(payments),
      bill_id: bill.id,
      verified_by_user_id: 1,
      receipt_no: `KW-2607-${String(nextId(payments)).padStart(3, "0")}`,
      amount_paid: bill.total_amount,
      payment_method: method,
      proof_image_url: null,
      payment_date: paymentDate,
      verified_at: paymentDate,
      notes: notes || (bill.discount_amount > 0 ? "Termasuk diskon saudara Rp 200.000" : null),
    };

    setPayments((current) => [payment, ...current]);
    setBills((current) =>
      current.map((item) =>
        item.id === bill.id ? { ...item, payment_status: "paid" } : item
      )
    );

    return payment;
  };

  const addStudent = (studentFields, { sppAmount, siblingDiscount, paymentMethod }) => {
    const studentId = nextId(students);
    const registrationDate = today();
    const student = {
      ...studentFields,
      id: studentId,
      registration_no: `ARH1-2026-${String(studentId).padStart(3, "0")}`,
      branch_id: 1,
      status: "active",
      registered_at: registrationDate,
    };
    const bill = {
      id: nextId(bills),
      student_id: student.id,
      academic_year_id: student.academic_year_id,
      bill_type: "spp_monthly",
      bill_period: registrationDate.slice(0, 7),
      base_amount: sppAmount,
      discount_amount: siblingDiscount,
      total_amount: Math.max(0, sppAmount - siblingDiscount),
      due_date: `${registrationDate.slice(0, 7)}-10`,
      payment_status: paymentMethod === "cash" || paymentMethod === "qris" ? "paid" : "unpaid",
    };

    setStudents((current) => [...current, student]);
    setBills((current) => [...current, bill]);

    if (bill.payment_status === "paid") {
      recordPaymentForBill(bill, { method: paymentMethod });
    }

    return student;
  };

  const recordPayment = (billId, paymentDetails) => {
    const bill = bills.find((item) => item.id === Number(billId));
    if (!bill) return null;
    return recordPaymentForBill(bill, paymentDetails);
  };

  const enrollStudent = (classId, studentId) => {
    const numericClassId = Number(classId);
    const numericStudentId = Number(studentId);
    const kelas = classes.find((item) => item.id === numericClassId);
    if (!kelas) return { ok: false, reason: "Kelas tidak ditemukan." };

    const existing = classEnrollments.find(
      (enrollment) =>
        enrollment.class_id === numericClassId &&
        enrollment.student_id === numericStudentId
    );
    if (existing?.enrollment_status === "active") {
      return { ok: false, reason: "Siswa sudah terdaftar aktif di kelas ini." };
    }
    if (kelas.current_students >= kelas.max_students) {
      return { ok: false, reason: "Kelas sudah penuh." };
    }

    if (existing?.enrollment_status === "waiting_list") {
      setClassEnrollments((current) =>
        current.map((enrollment) =>
          enrollment.id === existing.id
            ? { ...enrollment, enrollment_status: "active", enrolled_at: today() }
            : enrollment
        )
      );
    } else {
      setClassEnrollments((current) => [
        ...current,
        {
          id: nextId(current),
          class_id: numericClassId,
          student_id: numericStudentId,
          enrollment_status: "active",
          enrolled_at: today(),
        },
      ]);
    }

    return { ok: true };
  };

  const addPengeluaran = ({ kategori, keterangan, nominal, tanggal }) => {
    const nextNumber = Math.max(
      0,
      ...pengeluaran.map((item) => Number(String(item.id).replace(/^P/, "")) || 0)
    ) + 1;
    const expense = {
      id: `P${String(nextNumber).padStart(3, "0")}`,
      kategori,
      keterangan,
      nominal: Number(nominal),
      tanggal,
      status: "Menunggu",
    };

    setPengeluaran((current) => [...current, expense]);
    return expense;
  };

  const value = {
    students,
    classes,
    classEnrollments,
    bills,
    payments,
    pengeluaran,
    addStudent,
    enrollStudent,
    addPengeluaran,
    recordPayment,
  };

  return (
    <FrontdeskDataContext.Provider value={value}>
      {children}
    </FrontdeskDataContext.Provider>
  );
}

export function useFrontdeskData() {
  const context = useContext(FrontdeskDataContext);
  if (!context) {
    throw new Error("useFrontdeskData harus digunakan di dalam FrontdeskDataProvider.");
  }
  return context;
}

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

const today = () => {
  const date = new Date();
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
};
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
      classRecords.map((kelas) => {
        const currentStudents = classEnrollments.filter(
          (enrollment) =>
            enrollment.class_id === kelas.id &&
            enrollment.enrollment_status === "active"
        ).length;

        return {
          ...kelas,
          current_students: currentStudents,
          status:
            currentStudents >= kelas.max_students
              ? "full"
              : currentStudents >= Math.ceil(kelas.max_students * 0.8)
                ? "almost_full"
                : "open",
        };
      }),
    [classRecords, classEnrollments]
  );

  const recordPaymentForBill = (bill, { method, notes, paymentId } = {}) => {
    const paymentDate = today();
    const id = paymentId ?? nextId(payments);
    const payment = {
      id,
      bill_id: bill.id,
      verified_by_user_id: 1,
      receipt_no: `KW-2607-${String(id).padStart(3, "0")}`,
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

  const addStudent = (
    studentFields,
    { sppAmount, siblingDiscount, paymentMethod, modulAmount = 0 }
  ) => {
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
    const billId = nextId(bills);
    const billPeriod = registrationDate.slice(0, 7);
    const dueDate = `${billPeriod}-10`;
    const paymentStatus = paymentMethod === "cash" || paymentMethod === "qris" ? "paid" : "unpaid";
    const bill = {
      id: billId,
      student_id: student.id,
      academic_year_id: student.academic_year_id,
      bill_type: "spp_monthly",
      bill_period: billPeriod,
      base_amount: sppAmount,
      discount_amount: siblingDiscount,
      total_amount: Math.max(0, sppAmount - siblingDiscount),
      due_date: dueDate,
      payment_status: paymentStatus,
    };
    const moduleBill = modulAmount > 0
      ? {
          id: billId + 1,
          student_id: student.id,
          academic_year_id: student.academic_year_id,
          bill_type: "module_semester",
          bill_period: billPeriod,
          base_amount: modulAmount,
          discount_amount: 0,
          total_amount: modulAmount,
          due_date: dueDate,
          payment_status: paymentStatus,
        }
      : null;

    setStudents((current) => [...current, student]);
    setBills((current) => [...current, bill, ...(moduleBill ? [moduleBill] : [])]);

    if (bill.payment_status === "paid") {
      const paymentId = nextId(payments);
      recordPaymentForBill(bill, { method: paymentMethod, paymentId });
      if (moduleBill) {
        recordPaymentForBill(moduleBill, {
          method: paymentMethod,
          notes: "Biaya modul semester",
          paymentId: paymentId + 1,
        });
      }
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

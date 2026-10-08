---
id: TC-GS-DIV-E2E-032-edit-modal-auto-generate-code-saat-kosong
title: "Auto-Generate Code pada Form Edit Saat Dikosongkan Manual atau Spasi Saja, Serta Evaluasi No-Op Nilai Identik"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-98
  - TC-GS-DIV-99
  - TC-GS-DIV-288
coverage:
  web: automated
---

# Auto-Generate Code pada Form Edit Saat Dikosongkan Manual atau Spasi Saja, Serta Evaluasi No-Op Nilai Identik

## Prerequisites

- Login sebagai Role: Total Control
- Buka Edit Division
- User berada di Global Settings > User > Division
- Division `Accounting` (Code `ACC`) sudah dibuat (TC-GS-DIV-30)
- Division `Human Resources` dengan Code `HR` sudah ada
- Division `Information Technology` (Code `IT`) ada (TC-GS-DIV-30) dan Code `IT` hanya dipakai record itu sendiri

## Test Steps

### Edit dengan Code dikosongkan di-generate otomatis dan dicatat bila berbeda (TC-GS-DIV-98)

1. Buka row action baris `Customer Service` lalu klik `Edit`
2. Kosongkan Code
3. Klik `[Save]`
4. Lihat baris di tabel
5. Verifikasi Muncul toast sukses: `Success, division has been updated.`
6. Verifikasi Tabel menampilkan Code `CS` hasil auto-generate
7. Verifikasi Changelog mencatat perubahan Code `CSV` menjadi `CS`

### Edit dengan Code dikosongkan yang hasil generate identik dengan Code sendiri tidak berubah (TC-GS-DIV-99)

8. Buka row action baris `Human Resources` lalu klik `Edit`
9. Kosongkan Code
10. Klik `[Save]`
11. Verifikasi Kandidat `HR` hanya bentrok dengan record itu sendiri sehingga tidak dihitung bentrok
12. Verifikasi Muncul toast netral: `No changes to save.`
13. Verifikasi Modal menutup dan Code tetap `HR`
14. Verifikasi Tidak ada entri log baru

### Edit dengan Code berisi spasi saja dianggap kosong dan di-generate otomatis (TC-GS-DIV-288)

15. Buka row action baris `Information Technology` lalu klik `Edit`
16. Ganti Code dengan 3 spasi
17. Klik `[Save]`
18. Lihat baris di tabel
19. Verifikasi Tidak ada error pada Code
20. Verifikasi Kandidat `IT` hanya bentrok dengan record itu sendiri sehingga tidak dihitung bentrok; Code tetap `IT`
21. Verifikasi Muncul toast netral: `No changes to save.` dan modal menutup
22. Verifikasi Tidak ada entri log baru

## Notes

- Memvalidasi bahwa mengosongkan Code atau mengisi spasi saja pada Edit memicu auto-generate server-side (NC-02, DIV-LOGIC-04b), dan jika hasil generate identik dengan nilai tersimpan dihitung No-Op (PRD §9.2 [F-DIV-09]).
- Sumber pemetaan test case granular: TC-GS-DIV-98, TC-GS-DIV-99, TC-GS-DIV-288.

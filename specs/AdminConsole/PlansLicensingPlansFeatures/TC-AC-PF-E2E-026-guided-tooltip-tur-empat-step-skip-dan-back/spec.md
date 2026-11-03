---
id: TC-AC-PF-E2E-026-guided-tooltip-tur-empat-step-skip-dan-back
title: Guided Tooltip - Tur Empat Step, Skip, dan Back
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-44
  - TC-AC-PF-45
  - TC-AC-PF-46
coverage:
  web: automated
---

# Guided Tooltip - Tur Empat Step, Skip, dan Back

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`). Pre-setup #45 menyebut "akun baru tanpa flag" tanpa identitas; spec memakai akun #1 dengan flag dihapus (lihat Kemampuan teknis dan Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip: spec ini adalah pengecualian atas pernyataan di `suite.md`. Sesudah hook suite menyetel flag `guided_tooltip_seen_ac-plans-features` true, hook `before` spec ini menghapus flag itu untuk akun #1 sehingga tur tampil; hook `after` memulihkan nilai awal flag.
- Data Pre-setup: Dataset Plan A (Starter, Growth, Professional, Enterprise, SIEM aktif; kolom Clients tampil dengan konfigurasi kolom default; preferensi kolom browser dihapus di hook `before`).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk menghapus dan membaca flag Guided Tooltip akun aktor, pemulihan Dataset Pre-setup. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: flag Guided Tooltip akun #1; suite berjalan serial (`parallel: false`); dipulihkan di hook `after`.

## Test Steps

### TC-AC-PF-44 dan TC-AC-PF-46: tur empat step dan tombol Back

1. Pindah ke halaman lain di Admin Console lewat sidebar (tur yang mulai di hook `beforeEach` tertutup tanpa menandai flag).
2. Klik menu Plans & Licensing > Plans & Features di sidebar.
3. Verifikasi tur otomatis mulai di Step 1.
4. Verifikasi Step 1 menampilkan tombol `[Skip]` dan `[Next]` dan tanpa tombol `[Back]`.
5. Verifikasi Step 1: target Tabs navigasi.
6. Verifikasi Step 1: Title "Plan Catalog".
7. Verifikasi Step 1: Description "Switch between the plan lists to review current offerings and retired plans."
8. Klik `[Next]`.
9. Verifikasi Step 2: target Clients column.
10. Verifikasi Step 2: Title "Assigned Clients Count".
11. Verifikasi Step 2: Description "See how many clients each plan covers. Open Plan Detail to view the full client list."
12. Klik `[Back]`.
13. Verifikasi tur kembali ke Step 1 dengan Title "Plan Catalog".
14. Klik `[Next]`.
15. Klik `[Next]`.
16. Verifikasi Step 3: target Toolbar (Search & Filter).
17. Verifikasi Step 3: Title "Find a Plan".
18. Verifikasi Step 3: Description "Search or filter the list to find a specific plan quickly."
19. Klik `[Next]`.
20. Verifikasi Step 4: target Table — kolom `Actions` (header).
21. Verifikasi Step 4: Title "Plan Actions".
22. Verifikasi Step 4: Description "Open the actions menu on any row to work with a plan. What you can do depends on the sub-tab you are on and on your permissions. Push Update lives inside Plan Detail, not in this menu."
23. Verifikasi pada Step 4 tombol `[Next]` berubah menjadi `[Done]`.
24. Klik `[Done]`.
25. Verifikasi tur tertutup.

### TC-AC-PF-45: tombol Skip

26. Hapus flag `guided_tooltip_seen_ac-plans-features` akun #1 lewat fixture BE.
27. Pindah ke halaman lain di Admin Console lewat sidebar.
28. Klik menu Plans & Licensing > Plans & Features di sidebar sehingga tur mulai.
29. Klik `[Skip]` pada Step 1.
30. Verifikasi tur tertutup.
31. Muat ulang halaman (F5).
32. Verifikasi Breadcrumb halaman Plans & Features tampil.
33. Verifikasi tur tidak muncul lagi.

## Notes

- Langkah penghubung (S-03): langkah 1, 14, 15, 26, 27 dan 28. Langkah 1 dan 27 memenuhi precondition TC "User berada di halaman lain di Admin Console". Langkah 14 dan 15 melanjutkan tur ke Step 3 sesudah kembali ke Step 1. Langkah 26 menghapus flag yang diset TC-AC-PF-44 sebelum TC-AC-PF-45.
- Urutan TC: TC-AC-PF-46 (Back) dijalankan di dalam alur TC-AC-PF-44 karena precondition keduanya identik (flag belum ada, dari halaman lain); langkah 13 memenuhi Expected b TC-AC-PF-46 dan langkah 4 memenuhi Expected a TC-AC-PF-46 (Step 1 tanpa `[Back]`) sekaligus Expected b TC-AC-PF-44, sehingga tidak diulang. Menjalankan keduanya terpisah memerlukan tiga reset flag.
- Langkah 32 adalah anchor positif untuk langkah 33 (absence sesudah F5).
- Temuan untuk QA:
  - Pre-setup #45 menyebut "akun baru tanpa flag" tanpa identitas dan email akun; spec memakai akun #1 dengan flag dihapus lewat fixture BE (kemampuan disediakan tim FE/BE, mekanismenya tidak tertulis di TC, PRD, atau LLD).
  - Post Condition flag `guided_tooltip_seen_ac-plans-features` true (TC-AC-PF-44 dan TC-AC-PF-45) dan "Tidak ada perubahan data" (TC-AC-PF-46) tanpa langkah observasi di TC tidak diasersi (S-01).

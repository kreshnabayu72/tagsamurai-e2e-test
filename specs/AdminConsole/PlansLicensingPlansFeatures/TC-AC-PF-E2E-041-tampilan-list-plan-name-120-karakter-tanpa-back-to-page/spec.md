---
id: TC-AC-PF-E2E-041-tampilan-list-plan-name-120-karakter-tanpa-back-to-page
title: Tampilan List - Plan Name 120 Karakter, Tanpa Back to dan Page Title, serta Baris Archive Tanpa Muted
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-AC-PF-603
  - TC-AC-PF-726
  - TC-AC-PF-727
  - TC-AC-PF-728
  - TC-AC-PF-729
  - TC-AC-PF-749
  - TC-AC-PF-750
coverage:
  web: automated
---

# Tampilan List - Plan Name 120 Karakter, Tanpa Back to dan Page Title, serta Baris Archive Tanpa Muted

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite.
- Flag Guided Tooltip mengikuti pernyataan di `suite.md` (hook suite menyetel flag true untuk akun aktor pre-setup).
- Data Pre-setup: Dataset Plan A (default aktif Starter, Growth, Professional, Enterprise, SIEM; default archived `Growth Plus (old)`; custom Principal archived `Enterprise Reseller`). Spec hanya membaca data ini; nama literal tanpa suffix memakai pengecualian S-06/S-12 butir A-14 (nilai dirujuk lewat fixture data `fixtures/plans-licensing-plans-features.json` yang belum ada, ditandai di sini sesuai S-12).
- Data Dinamis (bersuffix per run): custom plan Principal aktif dengan Plan Name tepat 120 karakter termasuk suffix `{runId}-041`, dibuat di hook `before` lewat fixture BE (disediakan tim FE/BE) dan dibuang di hook `after` (archive lalu Delete). Teks nama lengkap disebut "nama 120 karakter" di langkah.
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk membuat dan membuang custom plan dengan nama 120 karakter. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: tidak ada yang diubah selain data milik spec; suite berjalan serial (`parallel: false`); konfigurasi kolom Setup Column tidak diubah.

## Test Steps

### TC-AC-PF-726: Plans List tanpa Back to dan Page Title

1. Verifikasi Breadcrumb tampil sebagai identitas dan navigasi halaman Plans List.
2. Verifikasi tidak ada tombol atau tautan `← Back to ...` pada Plans List.
3. Verifikasi tidak ada elemen Page Title terpisah di bawah breadcrumb.

### TC-AC-PF-749: sub-tab Archive tab Default tanpa muted

4. Hover baris pertama sub-tab Active.
5. Klik sub-tab Archive.
6. Hover baris `Growth Plus (old)`.
7. Verifikasi teks dan warna baris `Growth Plus (old)` di sub-tab Archive sama dengan baris sub-tab Active: tidak ada muted atau opacity tambahan.
8. Verifikasi satu-satunya perubahan visual baris Archive adalah state hover yang sama dengan state hover baris sub-tab Active pada langkah 4.

### TC-AC-PF-727: Plan Detail tanpa Back to dan Page Title

9. Klik sub-tab Active.
10. Buka Plan Detail `Growth` (klik Plan Name).
11. Verifikasi Breadcrumb tampil sebagai navigasi kembali.
12. Verifikasi tidak ada tombol atau tautan `← Back to ...` pada Plan Detail.
13. Verifikasi baris identitas plan pada Detail Header (`Growth – v5` dan Status Badge) tampil sebagai pengecualian §27.1b dan bukan Page Title.
14. Verifikasi tidak ada judul halaman tambahan di bawah breadcrumb.
15. Kembali ke list lewat Breadcrumb.

### TC-AC-PF-750: sub-tab Archive tab Custom tanpa muted

16. Klik tab Custom.
17. Hover baris pertama sub-tab Active.
18. Klik sub-tab Archive.
19. Hover baris `Enterprise Reseller`.
20. Verifikasi teks dan warna baris `Enterprise Reseller` di sub-tab Archive sama dengan baris sub-tab Active: tidak ada muted atau opacity tambahan.
21. Verifikasi satu-satunya perubahan visual baris Archive adalah state hover yang sama dengan state hover baris sub-tab Active pada langkah 17.

### TC-AC-PF-603: Plan Name 120 karakter

22. Klik sub-tab Active.
23. Ketik Search nama 120 karakter, tekan Enter.
24. Verifikasi nama tampil penuh (hug content, wrap natural) tanpa pemotongan `..`.
25. Hover teks nama 120 karakter.
26. Verifikasi tidak ada tooltip pada teks nama.
27. Verifikasi lebar kolom Plan Name mengikuti konten.
28. Klik `(←)` pada kotak Search.

### TC-AC-PF-728: Form Create Custom Plan tanpa Back to dan Page Title

29. Klik `+ Custom Plan`.
30. Verifikasi Breadcrumb tampil sebagai identitas dan navigasi halaman form Create Custom Plan.
31. Verifikasi tidak ada tombol atau tautan `← Back to ...` pada form.
32. Verifikasi tidak ada elemen Page Title terpisah di bawah breadcrumb.

### TC-AC-PF-729: tab Global Settings tanpa Back to dan Page Title

33. Kembali ke list lewat Breadcrumb.
34. Klik tab Global Settings.
35. Verifikasi Breadcrumb tampil sebagai navigasi kembali.
36. Verifikasi tidak ada tombol atau tautan `← Back to ...` pada tab Global Settings.
37. Verifikasi judul Card `FAMS` tampil sebagai header SectionCard.
38. Verifikasi tidak ada judul halaman tambahan di bawah breadcrumb.

## Notes

- Langkah penghubung (S-03): langkah 5, 9, 16, 18, 22, 34 (pindah tab dan sub-tab), langkah 15 dan 33 (kembali ke list), langkah 29 dan 10 (membuka form dan Plan Detail yang diasersi langkah berikutnya). Langkah 23 (Search untuk menemukan baris target) dan langkah 28 (mengosongkan Search) adalah langkah penghubung (R-16); langkah 4 dan 17 adalah baseline hover untuk Expected b.
- Urutan TC: TC-AC-PF-749 dan TC-AC-PF-750 disisipkan di antara TC-AC-PF-726, 727, 728, dan 729 per permukaan (Default, Custom, Global Settings) agar tiap permukaan dibuka sekali. Form Create Custom Plan pada langkah 29 dibuka tanpa input sehingga tidak dirty dan ditutup lewat Breadcrumb pada langkah 33.
- Alasan melewati sekitar 35 langkah: seluruh TC berkelas tampilan UI murni (UI Only) pada halaman yang sama dengan dataset yang sama, tiap blok berdiri sendiri, dan kegagalan satu blok tidak membuat blok lain kehilangan makna. Absence `← Back to ...` dan Page Title diverifikasi per surface (Plans List, Plan Detail, form Create, tab Global Settings), masing-masing dengan anchor Breadcrumb.
- Temuan untuk QA:
  - TC-AC-PF-603 menyebut "Custom plan dengan Plan Name 120 karakter tersedia" tanpa data di Pre-setup; nama dibuat spec lewat fixture BE.
  - TC-AC-PF-728 langkah 1 hanya membuka form lalu mengamati; TC tidak menyebut cara kembali ke list.
  - Post Condition "Tidak ada perubahan data" tanpa langkah observasi tidak diasersi (S-01).

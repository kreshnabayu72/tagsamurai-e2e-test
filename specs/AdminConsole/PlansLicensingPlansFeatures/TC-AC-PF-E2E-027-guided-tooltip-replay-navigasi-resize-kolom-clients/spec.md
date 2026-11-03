---
id: TC-AC-PF-E2E-027-guided-tooltip-replay-navigasi-resize-kolom-clients
title: Guided Tooltip - Replay Tombol [?], Navigasi, Resize, dan Kolom Clients Disembunyikan
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-AC-PF-47
  - TC-AC-PF-48
  - TC-AC-PF-49
coverage:
  web: automated
---

# Guided Tooltip - Replay Tombol [?], Navigasi, Resize, dan Kolom Clients Disembunyikan

## Prerequisites

- Mode: FE+BE
- Akun aktor: #1 `totalControlPrincipal_automated_{namaCompany}@qwertysystem.net` (Total Control, Principal; password dari env `AC_TC_PASSWORD`). TC-AC-PF-48 membutuhkan akun tanpa flag; spec memakai akun #1 dengan flag dihapus (lihat Temuan untuk QA).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Flag Guided Tooltip: TC-AC-PF-47 dan TC-AC-PF-49 berjalan dengan flag `guided_tooltip_seen_ac-plans-features` true (pernyataan di `suite.md`). Sebelum TC-AC-PF-48 flag dihapus lewat fixture BE (langkah 19); hook `after` memulihkan nilai awal flag.
- Data Pre-setup: Dataset Plan A (Starter, Growth, Professional, Enterprise, SIEM aktif; kolom Clients tampil).
- Kemampuan teknis (disediakan tim FE/BE, dinyatakan di `suite.md`): fixture backend untuk menghapus dan membaca flag Guided Tooltip akun aktor; kemampuan mengubah ukuran jendela browser. Fixture data `fixtures/plans-licensing-plans-features.json` belum ada (S-12).
- State global: flag Guided Tooltip akun #1, konfigurasi kolom Setup Column di browser (preferensi kolom dihapus di hook `after`), ukuran jendela browser (dipulihkan di langkah 31); suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-PF-47: tombol replay [?]

1. Hover tombol `[?]` di sebelah kanan breadcrumb.
2. Verifikasi tooltip tombol `[?]` bertuliskan `Show guide`.
3. Klik tombol `[?]`.
4. Verifikasi tur mulai dari Step 1.
5. Klik `[Skip]`.
6. Muat ulang halaman (F5).
7. Verifikasi Breadcrumb halaman Plans & Features tampil.
8. Verifikasi tur tidak otomatis muncul.
9. Verifikasi flag `guided_tooltip_seen_ac-plans-features` tetap true (dibaca lewat fixture BE).

### TC-AC-PF-49: Step 2 dilewati saat kolom Clients disembunyikan

10. Klik header kolom Actions (`⋯`).
11. Pada Overlay Column Visibility, uncheck kolom `Clients`.
12. Klik tombol `[?]` di sebelah kanan breadcrumb.
13. Klik `[Next]` dari Step 1.
14. Verifikasi tur menampilkan Title "Find a Plan" dengan indikator `Step 2 of 3` (Step Assigned Clients Count dilewati).
15. Verifikasi tidak ada error dan tidak ada spotlight pada elemen lain.
16. Klik `[Skip]`.
17. Klik header kolom Actions (`⋯`).
18. Pada Overlay Column Visibility, check kembali kolom `Clients`.

### TC-AC-PF-48: navigasi dan resize menutup tur tanpa menandai flag

19. Hapus flag `guided_tooltip_seen_ac-plans-features` akun #1 lewat fixture BE.
20. Pindah ke halaman lain di Admin Console lewat sidebar.
21. Klik menu Plans & Licensing > Plans & Features di sidebar sehingga tur mulai.
22. Klik menu Plans & Licensing > Plans & Features di sidebar lagi (navigasi) tanpa menyelesaikan tur.
23. Verifikasi tur tertutup saat navigasi.
24. Buka kembali halaman Plans & Features lewat menu Plans & Licensing > Plans & Features di sidebar.
25. Verifikasi tur muncul kembali dari Step 1.
26. Ubah ukuran jendela browser (resize).
27. Verifikasi tur tertutup saat resize.
28. Muat ulang halaman Plans & Features (F5).
29. Verifikasi tur muncul kembali dari Step 1.
30. Verifikasi flag `guided_tooltip_seen_ac-plans-features` belum true (dibaca lewat fixture BE).
31. Pulihkan ukuran jendela browser ke ukuran awal.

## Notes

- Langkah penghubung (S-03): langkah 16, 17, 18, 19, 20 dan 31. Langkah 16 sampai 18 menutup tur dan memulihkan kolom `Clients` sebelum TC berikutnya mengandalkannya; langkah 19 dan 20 memenuhi precondition TC-AC-PF-48 (flag belum ada, dari halaman lain).
- Urutan TC: TC-AC-PF-49 dijalankan sebelum TC-AC-PF-48 supaya flag true yang dipakai TC-AC-PF-47 dan TC-AC-PF-49 tidak perlu dihapus dua kali.
- Langkah 7 adalah anchor positif untuk langkah 8 (absence sesudah F5).
- Pembagian TC lintas spec: TC-AC-PF-645 ada di spec 045.
- Temuan untuk QA:
  - TC-AC-PF-48 langkah 2 dan 3 mengklik menu Plans & Features dua kali dari halaman yang sama tanpa pindah halaman di antaranya; TC tidak menyatakan apakah "Buka kembali halaman" berarti memuat ulang atau pindah halaman lain dulu. Spec mengikuti urutan TC (langkah 22 dan 24).
  - TC-AC-PF-48 membutuhkan "akun baru" tanpa flag tanpa identitas di Pre-setup; spec memakai akun #1 dengan flag dihapus lewat fixture BE (mekanismenya tidak tertulis di TC, PRD, atau LLD).
  - TC-AC-PF-49 Expected b ("tidak ada error dan tidak ada spotlight pada elemen lain") tidak menyebut elemen yang diamati; spec memverifikasinya pada tur Step 2 yang tampil (langkah 14).
  - Post Condition "Flag tetap true" (TC-AC-PF-47) sudah punya padanan Expected c; Post Condition "Flag belum true" (TC-AC-PF-48) punya padanan Expected d. Post Condition "Tidak ada perubahan data" (TC-AC-PF-49) tanpa langkah observasi tidak diasersi (S-01).

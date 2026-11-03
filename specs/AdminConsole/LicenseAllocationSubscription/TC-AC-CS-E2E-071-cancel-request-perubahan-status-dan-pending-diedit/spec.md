---
id: TC-AC-CS-E2E-071-cancel-request-perubahan-status-dan-pending-diedit
title: "Cancel Request: Perubahan Status dan Pending Diedit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-AC-CS-276
  - TC-AC-CS-547
  - TC-AC-CS-632
coverage:
  web: automated
---

# Cancel Request: Perubahan Status dan Pending Diedit

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup baca-saja/global: Toggle Require Approval for Allocation ON dan aktor bukan bypass (#23); tanggal acuan uji `19/08/26` (#28).
- Data seed milik aktor dan spec ini (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan PT Maju Bersama pada group `Jawa`, requester `Fajar N`, Plan Owner PT Maju Bersama; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed). Satu seed per blok TC:
  1. TC-AC-CS-276: Client `Apotek Sehat Sentosa A+{runId}-071` dengan term FAMS Growth Waiting for Approval (bentuk Pre-setup #49).
  2. TC-AC-CS-547: Client `Apotek Sehat Sentosa B+{runId}-071` dengan term berbentuk sama dengan seed TC-AC-CS-276.
  3. TC-AC-CS-632: Client `Apotek Sehat Sentosa C+{runId}-071` dengan term SIEM Pending, Start Date `15/09/26`, End Date `14/09/27`, Duration 1 year(s), hasil approval milik `Fajar N` (bentuk Pre-setup #90).
- Data Dinamis: hasil Approve, Cancel, Edit, dan entri audit trail hanya pada Client seed dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: jam server dan browser (hook `after`).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`) supaya Start Date seed `15/09/26` tetap di masa depan; sesi API aktor untuk Approve oleh approver dan Cancel oleh aktor yang sama (pelaku kedua, bukan sesi web); membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-276: Cancel Request ditolak saat pengajuan sudah berubah status

1. Ketik Search `Apotek Sehat Sentosa A+{runId}-071`, tekan Enter, klik ikon `⋯` pada baris Subscription ID seed Apotek Sehat Sentosa A lalu pilih `Cancel Request`
2. Approve pengajuan Subscription ID seed Apotek Sehat Sentosa A lewat sesi API aktor approver hingga status approved tersimpan, lalu klik `[Cancel Request]`
3. Verifikasi dialog blok Title "Cannot Cancel Request" dengan Body "• Apotek Sehat Sentosa A+{runId}-071 — FAMS" dan "This request has already been approved."
4. Verifikasi tombol tunggal `[OK]`
5. Klik `[OK]`
6. Verifikasi dialog blok tertutup
7. Verifikasi status baris Subscription ID seed Apotek Sehat Sentosa A tidak berubah akibat klik (tetap hasil Approve)

### TC-AC-CS-547: Cancel Request ditolak saat pengajuan sudah dibatalkan sesi lain

8. Ganti isi kotak search dengan `Apotek Sehat Sentosa B+{runId}-071`, tekan Enter, lalu catat jumlah entri Changelog Client `Apotek Sehat Sentosa B+{runId}-071` — FAMS sebagai baseline
9. Klik ikon `⋯` pada baris Subscription ID seed Apotek Sehat Sentosa B lalu pilih `Cancel Request`
10. Batalkan pengajuan yang sama lewat sesi API aktor yang sama hingga status Canceled tersimpan, lalu klik `[Cancel Request]` pada sesi pertama
11. Verifikasi dialog blok Title "Cannot Cancel Request" dengan Body "• Apotek Sehat Sentosa B+{runId}-071 — FAMS" dan "This request has already been canceled."
12. Verifikasi tombol tunggal `[OK]`
13. Klik `[OK]`
14. Klik tab `History`, ganti isi kotak search dengan `Apotek Sehat Sentosa B+{runId}-071`, tekan Enter
15. Verifikasi status tetap Canceled
16. Buka modal Changelog Client `Apotek Sehat Sentosa B+{runId}-071` — FAMS
17. Verifikasi hanya satu entri baru Action `Cancel Request` dibanding baseline (tanpa log ganda)

### TC-AC-CS-632: Term Pending yang di-Edit kembali ke Waiting for Approval lalu di-Cancel Request menampilkan strip pada Start Date dan End Date

18. Tutup modal Changelog, klik tab `Current`, ganti isi kotak search dengan `Apotek Sehat Sentosa C+{runId}-071`, tekan Enter, klik ikon `⋯` pada baris Subscription ID seed Apotek Sehat Sentosa C lalu pilih `Edit`
19. Ubah Duration dari `1` menjadi `2` lalu klik `[Save]`
20. Verifikasi toast sukses "Success, subscription has been updated."
21. Verifikasi status berubah dari Pending menjadi Waiting for Approval
22. Klik ikon `⋯` pada baris lalu pilih `Cancel Request`, kemudian klik `[Cancel Request]`
23. Verifikasi toast sukses "Success, your request has been canceled."
24. Klik tab `History`, ganti isi kotak search dengan `Apotek Sehat Sentosa C+{runId}-071`, tekan Enter
25. Verifikasi baris berstatus Canceled di tab `History`
26. Verifikasi kolom Start Date baris "—" (otorisasi sebelumnya tidak berlaku lagi setelah Edit)
27. Verifikasi kolom End Date baris "—"
28. Klik baris untuk membuka Subscription Detail
29. Verifikasi Subscription Detail menampilkan Start Date "—"
30. Verifikasi Subscription Detail menampilkan End Date "—"

## Notes

- Pelaku kedua (Approve dan Cancel dari sesi lain) lewat sesi API aktor adalah pelaku kedua, bukan konteks kedua; tidak memakai P-2 (KEPUTUSAN 2026-10-30).
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16), termasuk Search ulang sesudah pindah tab `History` dan `Current`; `Verifikasi` dialog blok tertutup sebagai anchor sebelum membaca status baris; tutup modal Changelog; log dicari berdasarkan Action dan Field, bukan posisi teratas (S-14).
- Temuan untuk QA: (1) TC-AC-CS-276 dan TC-AC-CS-547 menyebut "sesi approver" dan "sesi lain milik aktor yang sama" tanpa mekanisme; spec memakai sesi API aktor yang dinyatakan di `suite.md`. (2) TC-AC-CS-632 menyebut ACCS-LOGIC-01d (otorisasi tidak berlaku setelah Edit) sebagai dasar tanda "—" tanpa nilai tanggal sebelum Edit; spec mengasersi hasil akhir.

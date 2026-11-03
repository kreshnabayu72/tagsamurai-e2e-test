---
id: TC-AC-CS-E2E-059-edit-hasil-re-approval-dan-saldo
title: "Edit: Hasil Re-Approval dan Saldo"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-223
  - TC-AC-CS-224
  - TC-AC-CS-229
  - TC-AC-CS-230
coverage:
  web: automated
---

# Edit: Hasil Re-Approval dan Saldo

## Prerequisites

- Mode: FE+BE.
- Akun aktor awal (login di hook `before`): capability Create saja Distributor PT Maju Bersama, Fajar Nugroho (Pre-setup #6), `createOnlySub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_CREATE_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Akun berikutnya (ganti akun eksplisit di Test Steps): Additional Approver Manage allocation Principal PT ABC, Maya Tanjung (Pre-setup #4), `approverSub_automated_{namaCompany}@qwertysystem.net` (dirujuk lewat `Fixture.license-allocation-subscription`, belum ada, disediakan tim FE; kredensial `Spectra.env.AC_SUB_APPROVER_PASSWORD`, nama didaftarkan di `executionConfig.environmentVariables` dan `.env.example`).
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Allocation > Client Subscription, tab Current). Hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Hook suite yang dirujuk spec ini dan dinyatakan sekali di `suite.md`: flag Guided Tooltip `guided_tooltip_seen_ac-license-allocation-subscription` disetel `seen` di hook `before` dan dipulihkan di hook `after`, sesi API aktor untuk pelaku kedua dan aksi pemicu, serta fixture backend pemulihan state Pre-setup.
- Suite serial: `parallel: false` (lihat `suite.md`).
- Data Pre-setup baca-saja/global: Toggle Require Approval for Allocation ON (#23) dan aktor bukan bypass; Main Pocket PT Maju Bersama (#20); tanggal acuan uji `19/08/26` (#28).
- Data seed milik spec (dibuat lewat API di hook `before`, dihapus di hook `after`; Client binaan PT Maju Bersama pada group `Jawa`; Subscription ID tiap term dibaca lewat API seeding dan dirujuk di langkah sebagai Subscription ID seed A sampai D):
  1. Seed A (TC-AC-CS-229): Client `Apotek Sehat Sentosa A+{runId}-059` dengan term FAMS Growth Waiting for Approval, Duration 1 year(s), snapshot harga $4,000.00 per tahun, Reserve $4,000.00, requester `Fajar N`, Plan Owner PT Maju Bersama (bentuk Pre-setup #49).
  2. Seed B (TC-AC-CS-230): Client `Apotek Sehat Sentosa B+{runId}-059` dengan term berbentuk sama dengan seed A.
  3. Seed C (TC-AC-CS-223): Client `Apotek Sehat Sentosa C+{runId}-059` dengan term berbentuk sama dengan seed A.
  4. Seed D (TC-AC-CS-224): Client `Apotek Sehat Sentosa D+{runId}-059` dengan term SIEM Pending, Start Date `15/09/26`, End Date `14/09/27`, Duration 1 year(s), Reserve $6,000.00, requester `Fajar N` hasil approval (bentuk Pre-setup #90).
- Data Dinamis: hasil Edit, Approve oleh sesi API, dan entri audit trail hanya pada Client seed A sampai D dan dihapus bersama seed di hook `after`. Yang dipulihkan hanya state global: saldo Main Pocket PT Maju Bersama (diubah TC-AC-CS-229 untuk memicu penolakan saldo, dipulihkan oleh fixture backend pemulihan state di langkah penghubung dan di hook `after`; tidak dapat dimiliki spec karena Wallet bersama) dan jam server dan browser (hook `after`).
- Kemampuan teknis (disediakan tim FE/BE): fixture waktu untuk tanggal acuan `19/08/26` (jam server dan jam browser, dipulihkan di hook `after`) supaya Start Date seed D `15/09/26` tetap di masa depan; membaca saldo Reserved dan Available Wallet Main Pocket; mengatur saldo Main Pocket kurang dari tambahan Reserve; sesi API aktor Approve pengajuan (pelaku approver); membaca jumlah entri Changelog.

## Test Steps

### TC-AC-CS-229: Saldo tidak cukup untuk Reserve baru menolak Edit

1. Atur saldo Main Pocket PT Maju Bersama kurang dari tambahan Reserve lewat fixture backend
2. Ketik Search `Apotek Sehat Sentosa A+{runId}-059`, tekan Enter
3. Klik ikon `⋯` pada baris Subscription ID seed A lalu pilih `Edit`
4. Ubah Duration menjadi `20` lalu klik `[Save]`
5. Verifikasi dialog blok dengan Title "Cannot Update Subscription"
6. Verifikasi Body "• Apotek Sehat Sentosa A+{runId}-059 — FAMS" dan "Insufficient wallet balance"
7. Verifikasi tombol tunggal `[OK]`
8. Klik `[OK]`, klik `[✕]`, verifikasi dialog Unsaved Changes, lalu klik `[Leave]`
9. Klik ikon `⋯` pada baris Subscription ID seed A lalu pilih `Edit`
10. Verifikasi Duration tersimpan tetap `1` (data lama tidak berubah)
11. Klik `[✕]`

### TC-AC-CS-230: Save ditolak saat term sudah diputuskan atau berubah status

12. Pulihkan saldo Main Pocket ke keadaan awal lewat fixture backend
13. Ganti isi kotak search dengan `Apotek Sehat Sentosa B+{runId}-059`, tekan Enter
14. Klik ikon `⋯` pada baris Subscription ID seed B lalu pilih `Edit`
15. Approve term Subscription ID seed B lewat sesi API aktor Additional Approver hingga status approved tersimpan
16. Klik `[Save]` pada form Edit
17. Verifikasi dialog blok dengan Title "Cannot Update Subscription"
18. Verifikasi Body "• Apotek Sehat Sentosa B+{runId}-059 — FAMS" dan "This request can no longer be edited."
19. Verifikasi tombol tunggal `[OK]`
20. Klik `[OK]`
21. Verifikasi dialog blok tertutup
22. Verifikasi status baris tidak berubah akibat Save (tetap hasil Approve)

### TC-AC-CS-223: Edit Duration pada term Waiting for Approval menghitung ulang biaya tanpa mereset SLA

23. Ganti isi kotak search dengan `Apotek Sehat Sentosa C+{runId}-059`, tekan Enter, lalu catat jumlah entri Changelog Client `Apotek Sehat Sentosa C+{runId}-059` — FAMS sebagai baseline
24. Klik ikon `⋯` pada baris Subscription ID seed C lalu pilih `Edit`
25. Ubah Duration menjadi `2`
26. Verifikasi Estimated Cost dihitung dari snapshot harga saat term dibuat: $8,000.00 (2 year(s) × $4,000.00/year)
27. Klik `[Save]`
28. Verifikasi toast sukses "Success, subscription has been updated."
29. Verifikasi status baris tetap Waiting for Approval
30. Verifikasi SLA approval tidak di-reset
31. Verifikasi Reserve term disesuaikan dari $4,000.00 menjadi $8,000.00
32. Buka modal Changelog Client `Apotek Sehat Sentosa C+{runId}-059` — FAMS
33. Verifikasi jumlah entri Changelog bertambah dibanding baseline
34. Verifikasi entri Changelog baru dengan Action `Edit (Duration, mode New/Renewal)`, Field `Duration`, Old `1 year(s)`, dan New `2 year(s)`

### TC-AC-CS-224: Edit term Pending dengan toggle ON kembali ke Waiting for Approval

35. Tutup modal Changelog, ganti isi kotak search dengan `Apotek Sehat Sentosa D+{runId}-059`, tekan Enter, lalu catat jumlah entri Changelog Client `Apotek Sehat Sentosa D+{runId}-059` — SIEM sebagai baseline
36. Klik ikon `⋯` pada baris Subscription ID seed D lalu pilih `Edit`
37. Ubah Duration dari `1` menjadi `2`
38. Klik `[Save]`
39. Verifikasi toast sukses "Success, subscription has been updated."
40. Verifikasi status berubah dari Pending menjadi Waiting for Approval
41. Verifikasi siklus approval baru dan SLA baru tercatat pada term
42. Buka modal Changelog Client `Apotek Sehat Sentosa D+{runId}-059` — SIEM
43. Verifikasi jumlah entri Changelog bertambah dibanding baseline
44. Verifikasi entri Changelog baru dengan Action `Edit (term `pending` kembali ke approval)`, Field `Status`, Old `Pending`, dan New `Waiting for Approval`
45. Tutup modal Changelog. Ganti akun: Logout lalu login sebagai Additional Approver Manage allocation Principal (`Maya Tanjung`) dan buka notifikasi
46. Verifikasi notifikasi "Subscription needs approval" untuk Subscription ID seed D terkirim ke approver pool

## Notes

- Urutan menyimpang dari urutan TC sumber (S-10): penolakan Save (TC-AC-CS-229, TC-AC-CS-230) didahulukan sebelum Edit sukses (TC-AC-CS-223, TC-AC-CS-224); TC-AC-CS-224 paling akhir karena ganti akun ke approver untuk notifikasi.
- Pelaku kedua yang Approve lewat sesi API (TC-AC-CS-230) bukan konteks kedua; tidak memakai P-2 (KEPUTUSAN 2026-10-30).
- Langkah penghubung (S-03): Search untuk menemukan baris target (R-16); pemulihan saldo Wallet lewat fixture; `✕`, dialog `Unsaved Changes`, dan `[Leave]` menutup form dirty (S-08, S-09); ganti akun eksplisit (S-07); `Verifikasi` dialog blok tertutup sebagai anchor sebelum membaca status baris (8b.8). Tutup modal Changelog sebelum aksi berikutnya. `Verifikasi` jumlah entri Changelog bertambah dibanding baseline menjalankan S-12 untuk asersi "entri baru".
- Temuan untuk QA: (1) TC-AC-CS-223 butir c dan TC-AC-CS-224 butir b ("SLA approval tidak di-reset", "SLA baru") tidak punya cara pengamatan di TC; spec mengasersinya sebagai tercatat tanpa nilai angka. (2) TC-AC-CS-223 dan TC-AC-CS-224 Post Condition (Reserve Wallet; pengajuan di Approvals) tanpa langkah observasi sehingga tidak diasersi, kecuali Reserve term yang sudah menjadi Expected d. (3) TC-AC-CS-229 tidak menyebut saldo Main Pocket sebelum Edit; spec memakai kemampuan "disediakan tim FE/BE". (4) TC-AC-CS-230 tidak menyebut hasil akhir record setelah Save ditolak; spec mengasersi tidak berubah dari hasil Approve.
- Spec ini 46 langkah, di atas smell 35 langkah. Alasan: semua blok satu topik (hasil Edit dan penolakan Save) pada record milik aktor yang sama, tanpa kelas harness lain; bagian pertama tidak membuat bagian lain kehilangan makna.

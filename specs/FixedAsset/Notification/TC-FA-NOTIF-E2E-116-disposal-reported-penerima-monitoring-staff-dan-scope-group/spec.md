---
id: TC-FA-NOTIF-E2E-116-disposal-reported-penerima-monitoring-staff-dan-scope-group
title: "Penerima Notifikasi Disposal Reported: Monitoring & Report Tidak Menerima, Staff dan Asset Admin Menerima, Approver di Luar Scope Tidak Menerima"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-NOTIF-320
  - TC-FA-NOTIF-321
coverage:
  web: automated
---
# Penerima Notifikasi Disposal Reported: Monitoring & Report Tidak Menerima, Staff dan Asset Admin Menerima, Approver di Luar Scope Tidak Menerima

## Prerequisites

- Mode: FE+BE.
- Akun yang login di UI (urutan baris = urutan pemakaian pada langkah):

  | Role | Pre-setup | Email | Env var password | Fixture |
  |---|---|---|---|---|
  | Monitoring & Report (Transaction Role Disposal, Gedung A) | #10 | `monitoringReport_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_MONREP_PASSWORD` | `Fixture.fixedAssetNotification.monitoringReport` |
  | Approver (Disposal, Gedung A) | #6 | `approverDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSP_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposal` |
  | Staff (Transaction Role Staff Disposal, Gedung A) | #9 | `staffDisposal_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_STAFFDSP_PASSWORD` | `Fixture.fixedAssetNotification.staffDisposal` |
  | Asset Admin (Gedung A) | #8 | `assetAdmin_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_ASSETADMIN_PASSWORD` | `Fixture.fixedAssetNotification.assetAdmin` |
  | Approver (Disposal) Gedung B (di luar scope group aset) | tidak ada di Pre-setup TC (akun disediakan tim FE) | `approverDisposalGedungB_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_APPROVERDSPB_PASSWORD` | `Fixture.fixedAssetNotification.approverDisposalGedungB` |

- Pelaku pemicu lewat sesi API aktor (butir "Sesi API aktor" di `suite.md`): Asset Admin (Gedung A) (Pre-setup #8, `assetAdmin_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_ASSETADMIN_PASSWORD`). Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan.
- Login akun aktor pertama (Monitoring & Report (Transaction Role Disposal, Gedung A), Pre-setup #10) di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit. Hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Data Pre-setup (tetap di environment): aset Kendaraan Operasional AST-2024-0088 In Use di Gedung A (Pre-setup #22 dan #24); Approver (Disposal) Gedung A Pre-setup #6; Monitoring & Report Pre-setup #10; Staff Pre-setup #9. Approver (Disposal) di Gedung B (di luar scope group aset) tidak ada di Pre-setup TC; akun disediakan tim FE. Spec mengubah aset menjadi ter-report; fixture BE pemulih mengembalikannya di awal tiap blok.
- Pengecualian S-06/S-12 butir A-16 (Lampiran A): langkah Report Disposal pada aset AST-2024-0088 (Pre-setup #22 dan #24) milik Pre-setup bersama yang dipulihkan Fixture BE (idempotent) di hook `before` dan `after` serta sebagai langkah penghubung antar blok; suite berjalan serial.
- Kemampuan teknis (disediakan tim FE/BE, tanpa endpoint karangan): fixture BE pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 serta penyetel state sumber (butir "Fixture BE pemulih seed notifikasi dan transaksi" dan "Fixture BE pemicu event dan penyetel state sumber" di `suite.md`); kemampuan baca BE atas jumlah item `Asset reported for disposal` per penerima (baseline dan selisih).
- Asersi absence atas notifikasi in-app memakai baseline jumlah item `Asset reported for disposal` per penerima (kemampuan baca BE) yang dicatat sebelum pemicu, anchor positif (penerima sah menerima item), dan jendela "Tunggu 5 detik tanpa memuat ulang halaman" yang merupakan pilihan spec (bukan nilai TC atau PRD).
- Item pembanding sebelum asersi absence: Monitoring & Report (Pre-setup #10) punya item seed pembanding `Asset has been repaired` (Read, view-only) menurut Pre-setup #17, disediakan fixture BE; `Verifikasi` Dropdown Panel memuat item itu mendahului asersi item `"Asset reported for disposal"` tidak tampil (bagian 8b butir 2 dan 11). Approver (Disposal) Gedung B tidak punya seed yang dijamin Pre-setup, sehingga anchor absence-nya adalah jumlah awal seluruh item notifikasi akun itu (kemampuan baca BE, surface agregat) ditambah `Verifikasi` Dropdown Panel termuat.
- State yang diubah spec dipulihkan hook `after` lewat fixture BE pemulih seed dan transaksi; efek tiap blok TC ditulis pada langkah penyiapan kondisi data.
- Flag Guided Tooltip `guided_tooltip_seen_fa-notification` true untuk semua akun di atas: hook suite `before` men-set dan `after` memulihkannya (butir "Flag Guided Tooltip" di `suite.md`).
- Env var `FA_MONREP_PASSWORD`, `FA_APPROVERDSP_PASSWORD`, `FA_STAFFDSP_PASSWORD`, `FA_ASSETADMIN_PASSWORD`, `FA_APPROVERDSPB_PASSWORD` (nama env usulan) didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`. Password tidak ditulis di spec atau fixture.
- Berkas `fixtures/fixedAssetNotification.json` belum ada; disediakan tim FE (nama kunci ditetapkan tim FE).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-NOTIF-320: disposal_reported tidak diterima Monitoring & Report

1. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Aset Kendaraan Operasional (AST-2024-0088) In Use di Gedung A
2. Catat jumlah item `"Asset reported for disposal"` milik Monitoring & Report (Pre-setup #10) sebagai baseline lewat kemampuan baca BE
3. Dari akun Asset Admin (Pre-setup #8, sesi API), Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan hingga laporan tersimpan
4. Ganti akun: logout, lalu login sebagai Approver (Disposal, Gedung A) (Pre-setup #6) dengan `Spectra.env.FA_APPROVERDSP_PASSWORD`, lalu buka Fixed Asset > Dashboard
5. Klik Bell icon
6. Verifikasi item `"Asset reported for disposal"` dengan Body `"Kendaraan Operasional (AST-2024-0088) was reported for disposal."` tampil pada Dropdown Panel Approver (Disposal) (anchor positif)
7. Ganti akun: logout, lalu login sebagai Monitoring & Report (Transaction Role Disposal, Gedung A) (Pre-setup #10) dengan `Spectra.env.FA_MONREP_PASSWORD`, lalu buka Fixed Asset > Dashboard
8. Tunggu 5 detik tanpa memuat ulang halaman
9. Klik Bell icon
10. Verifikasi Dropdown Panel Monitoring & Report tampil
11. Verifikasi Dropdown Panel Monitoring & Report memuat item seed pembanding `Asset has been repaired` (Read, view-only) milik akun itu (item pembanding pada surface yang sama, anchor absence)
12. Verifikasi item `"Asset reported for disposal"` tidak tampil pada Dropdown Panel Monitoring & Report
13. Verifikasi jumlah item `"Asset reported for disposal"` milik Monitoring & Report sama dengan baseline langkah 2 (dibaca lewat kemampuan baca BE yang sama)

### TC-FA-NOTIF-321: disposal_reported diterima sisi maker dan sisi approver dalam scope group aset

14. Siapkan kondisi data lewat fixture BE (pemulih seed notifikasi dan transaksi Pre-setup #17 sampai #24 dan penyetel state sumber): Aset Kendaraan Operasional (AST-2024-0088) In Use di Gedung A
15. Catat jumlah item `"Asset reported for disposal"` milik Approver (Disposal) Gedung B sebagai baseline lewat kemampuan baca BE, dan jumlah seluruh item notifikasi akun itu (surface agregat) sebagai jumlah awal agregat
16. Dari akun Asset Admin (Pre-setup #8, sesi API), Report Disposal aset AST-2024-0088 dari Asset Detail sebagai flag ringan hingga laporan tersimpan
17. Ganti akun: logout, lalu login sebagai Staff (Transaction Role Staff Disposal, Gedung A) (Pre-setup #9) dengan `Spectra.env.FA_STAFFDSP_PASSWORD`, lalu buka Fixed Asset > Dashboard
18. Klik Bell icon
19. Verifikasi item `"Asset reported for disposal"` dengan Body `"Kendaraan Operasional (AST-2024-0088) was reported for disposal."` tampil pada Dropdown Panel Staff
20. Ganti akun: logout, lalu login sebagai Asset Admin (Gedung A) (Pre-setup #8) dengan `Spectra.env.FA_ASSETADMIN_PASSWORD`, lalu buka Fixed Asset > Dashboard
21. Klik Bell icon
22. Verifikasi item `"Asset reported for disposal"` dengan Body `"Kendaraan Operasional (AST-2024-0088) was reported for disposal."` tampil pada Dropdown Panel Asset Admin Gedung A
23. Ganti akun: logout, lalu login sebagai Approver (Disposal) Gedung B (di luar scope group aset) (`approverDisposalGedungB_automated_{namaCompany}@qwertysystem.net`, akun disediakan tim FE; tidak tertulis di Pre-setup TC) dengan `Spectra.env.FA_APPROVERDSPB_PASSWORD`, lalu buka Fixed Asset > Dashboard
24. Tunggu 5 detik tanpa memuat ulang halaman
25. Klik Bell icon
26. Verifikasi Dropdown Panel Approver (Disposal) Gedung B tampil
27. Verifikasi (kemampuan baca BE) jumlah seluruh item notifikasi milik Approver (Disposal) Gedung B sama dengan jumlah awal agregat langkah 15 (anchor absence akun tanpa seed Pre-setup: surface agregat; Dropdown Panel termuat sudah diverifikasi langkah 26)
28. Verifikasi item `"Asset reported for disposal"` tidak tampil pada Dropdown Panel Approver (Disposal) Gedung B
29. Verifikasi jumlah item `"Asset reported for disposal"` milik Approver (Disposal) Gedung B sama dengan baseline langkah 15 (dibaca lewat kemampuan baca BE yang sama)

## Notes

- Langkah penghubung (S-03): langkah 1, 14 (penyiapan kondisi data lewat fixture BE); langkah 2, 15 (baseline jumlah item per penerima, S-12); langkah 4, 7, 17, 20, 23 (ganti akun dan buka Fixed Asset > Dashboard); langkah 8, 24 (jendela 5 detik tanpa memuat ulang halaman (bagian 6 konvensi)).
- Baseline per penerima yang tidak boleh menerima (Monitoring & Report dan Approver Gedung B) dicatat tepat sebelum pemicu (langkah 2 dan 15, bagian 8b butir 10); selisihnya diasersi pada langkah 13 dan 29. Anchor positif mendahului tiap asersi absence (langkah 6 dan 19 sampai 22). Langkah 10 dan 26 (Dropdown Panel tampil) serta langkah 13 dan 29 adalah asersi tambahan di luar Expected TC (S-03).
- Asersi tambahan di luar Expected TC (S-03): langkah 11 (item seed pembanding `Asset has been repaired` (Read, view-only) milik Monitoring & Report pada Dropdown Panel yang sama, anchor absence) dan langkah 27 (jumlah awal agregat akun Gedung B tanpa seed Pre-setup, anchor absence) ditulis sebelum asersi absence supaya asersi tidak lulus hampa.
- Spec 116 dan 065 sama-sama memakai AST-2024-0088; spec 116 menguji cakupan penerima per role (termasuk absence), sedangkan spec 065 menguji item dan tautan penerima, sehingga aset dipulihkan fixture BE di awal tiap blok.
- Temuan untuk QA:
  - Kolom Post Condition semua TC di spec ini kosong (`-`); tidak ada yang diasersi.
  - TC menulis "Picu: ..." tanpa menyebut akun atau endpoint pelaku; spec memakai fixture BE pemicu event atau sesi API aktor yang disediakan tim FE/BE (S-13), dan akun pelaku yang tertulis di Prerequisites diambil dari tabel Pre-setup.
  - TC-FA-NOTIF-321 menulis "Approver (Disposal) di Gedung B (di luar scope)" tanpa akun di tabel Pre-setup (Pre-setup #32 hanya Approver Borrowing & Assignment dan Transfer); akun disediakan tim FE, tanpa karangan.
  - TC-FA-NOTIF-320 dan 321 tidak menyebut Title item pada Expected 321 (a); spec memakai Title `Asset reported for disposal` dari TC-FA-NOTIF-254.

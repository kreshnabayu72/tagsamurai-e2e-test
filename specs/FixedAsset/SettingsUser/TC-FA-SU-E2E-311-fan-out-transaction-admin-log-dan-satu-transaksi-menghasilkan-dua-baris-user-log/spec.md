---
id: TC-FA-SU-E2E-311-fan-out-transaction-admin-log-dan-satu-transaksi-menghasilkan-dua-baris-user-log
title: "Fan-out Transaction Admin Log dan Satu Transaksi Menghasilkan Dua Baris User Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-SU-955
  - TC-FA-SU-956
coverage:
  web: automated
---

# Fan-out Transaction Admin Log dan Satu Transaksi Menghasilkan Dua Baris User Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Lina Marlina (Pre-setup #1), `totalControl_automated_{namaCompany}@qwertysystem.net`, kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman Fixed Asset > Settings > User dibuka hook `beforeEach` suite.
- Hook suite (`suite.md`) berlaku: flag Guided Tooltip User List `seen`, sesi API aktor untuk pelaku kedua, dan pemulihan Pre-setup bersama lewat seed API.
- Data Pre-setup: Client `FaUserMain` (#20), Transaction Admin Log (#29), dan User Log (#30). Nama dan atribut Pre-setup dirujuk lewat fixture `Fixture.fixedAssetSettingsUser.<kunci>` (berkas `fixtures/fixed-asset-settings-user.json` belum ada dan disediakan tim FE).
- Pengguna milik spec (dibuat lewat seed API di hook `before` dengan keadaan sama seperti pengguna Pre-setup bernama sama, dihapus di hook `after`; pengguna Pre-setup bersama tidak diubah, S-06; entri log permanen tidak dibersihkan):
  - `Budi Santoso {runId}-311`, email `budi.santoso+{runId}-311@qwertysystem.net`: Active; Transaction Role sebagai PIC pada modul Borrow; sub-tab Transaction Admin Log Borrowing & Assignment kosong sebelum transaksi (TC-FA-SU-955).
  - `Budi Santoso {runId}-311-2`, email `budi.santoso+{runId}-311-2@qwertysystem.net`: Active; riwayat User Log dari seed: sub-tab Borrow satu transaksi (`Borrowed` dan `Returned`), sub-tab Assignment satu transaksi (`Assigned` dan `Unassigned`), sub-tab Session satu sesi selesai (`Session started` dan `Session ended`); kredensial login disediakan tim FE (TC-FA-SU-956).
  - Aset milik spec `Aset Uji {runId}-311` untuk transaksi Borrow.
- Kemampuan transaksi lintas modul (disediakan tim FE/BE, tanpa endpoint karangan): membuat permohonan Borrow, Return, Assignment, dan Transfer, memproses persetujuan, dan membuat task konfirmasi untuk pengguna target; pelaku kedua (Budi Santoso sebagai approver atau PIC) lewat sesi API, ditulis "... hingga ... tersimpan" (R-20), bukan konteks UI kedua.
- Konteks browser kedua (pemicu): login `Budi Santoso {runId}-311-2` tanpa logout untuk memunculkan baris `Session started` (TC-FA-SU-956); konteks itu hanya memicu state, tanpa asersi di dalamnya, dan ditutup di hook `after` (S-09, `P-2`).
- Tidak ada intercept, jam server, atau klien HTTP. State global: tidak ada; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-SU-955: Tab Transaction Admin Log adalah fan-out per Jenis Transaksi dan bukan tampilan terfilter Tab System Log

1. Catat jumlah entri Tab System Log Budi Santoso {runId}-311 sebagai baseline
2. Proses transaksi Borrow aset Aset Uji {runId}-311 sebagai PIC Budi Santoso {runId}-311 lewat sesi API hingga transaksi tersimpan
3. Tunggu aksi selesai, lalu Search `Budi Santoso {runId}-311`, tekan Enter, klik nama Budi Santoso {runId}-311, dan buka Tab Transaction Admin Log > sub-tab Borrowing & Assignment
4. Verifikasi transaksi yang diproses Budi Santoso {runId}-311 sebagai PIC muncul pada sub-tab Borrowing & Assignment
5. Verifikasi tabel memuat kolom Transaction ID, Group, Role, Action Taken, Date, dan Transaction Status
6. Klik Transaction ID transaksi itu
7. Verifikasi klik Transaction ID tidak melakukan apa pun (halaman tidak berpindah)
8. Verifikasi Tab Transaction Admin Log tidak menyediakan aksi tulis
9. Buka Tab System Log
10. Verifikasi header kolom Tab System Log tampil
11. Verifikasi jumlah entri Tab System Log Budi Santoso {runId}-311 sama dengan baseline (transaksi tidak diduplikasi di Tab System Log)

### TC-FA-SU-956: Tab User Log: satu transaksi menghasilkan hingga dua baris dan sesi berlangsung hanya Session started

12. Search `Budi Santoso {runId}-311-2`, tekan Enter, klik nama Budi Santoso {runId}-311-2, lalu buka Tab User Log
13. Verifikasi sub-tab Borrow memuat satu transaksi dengan baris `Borrowed` dan `Returned`
14. Buka sub-tab Assignment
15. Verifikasi sub-tab Assignment memuat baris `Assigned` dan `Unassigned`
16. Buka sub-tab Session
17. Verifikasi sub-tab Session memuat `Session started` dan `Session ended`
18. Catat jumlah baris `Session started` dan jumlah baris `Session ended` pada sub-tab Session
19. Buka konteks browser kedua dan login sebagai Budi Santoso {runId}-311-2 tanpa logout
20. Kembali ke konteks aktor, lalu muat ulang sub-tab Session
21. Verifikasi jumlah baris `Session started` bertambah satu dari baseline
22. Verifikasi jumlah baris `Session ended` sama dengan baseline (sesi yang masih berlangsung hanya `Session started`)

## Notes

- Sumber: `fixed-asset/settings-user/TestCases/tc-settings-user.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (tanpa awalan `Verifikasi`, S-03): 3, 9, 12, 14, 16, 19, 20; langkah baseline jumlah entri (S-12): 1, 18. Langkah 3 dan 12 juga Search untuk menemukan baris target (R-16).
- `P-2`: konteks browser kedua (login Budi Santoso {runId}-311-2) pada langkah 19 hanya memicu baris `Session started` dan bukan objek asersi; asersi dilakukan di konteks aktor.
- Klausa "tanpa duplikasi di Tab System Log" TC-FA-SU-955 ditulis sebagai asersi jumlah dengan baseline dan anchor header kolom (S-12), bukan asersi absence kelas g.
- Pengguna dan aset milik spec bernama sama dengan Pre-setup TC dengan suffix `{runId}-311` (S-06).
- Temuan untuk QA (S-15):
  - TC-FA-SU-955 tidak menyebut sub-tab Jenis Transaksi yang diperiksa selain "yang bersangkutan"; spec memakai Borrowing & Assignment karena hanya sub-tab itu yang punya data Pre-setup (#29, Catatan TC). Nilai Action Taken dan Transaction Status tidak diasersi (NC-23).
  - TC-FA-SU-956 butir a dan b (`Borrowed`, `Returned`, `Assigned`, `Unassigned`) tidak menyebut data uji pemicunya; spec memakai riwayat seed milik spec. Pada langkah Uji "Login sebagai Budi tanpa logout", jam dan detail login tidak disebut TC.

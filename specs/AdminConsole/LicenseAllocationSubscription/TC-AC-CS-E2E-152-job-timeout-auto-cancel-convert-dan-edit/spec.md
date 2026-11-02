---
id: TC-AC-CS-E2E-152-job-timeout-auto-cancel-convert-dan-edit
title: "Job: Timeout Auto-Cancel Term Convert dan Edit"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-548
  - TC-AC-CS-633
coverage:
  web: automated
---

# Job: Timeout Auto-Cancel Term Convert dan Edit

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Fajar Nugroho, Create-Only Distributor PT Maju Bersama (Pre-setup #6), password `Spectra.env.AC_SUB_CREATE_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control Principal, Pre-setup #1).
- Email akun dirujuk lewat `Fixture.license-allocation-subscription` (fixture disediakan tim FE); password hanya lewat env, tidak ditulis di spec atau fixture.
- Data Dinamis (bersuffix `{runId}-152`): term paid Waiting for Approval hasil Convert jalur request milik Fajar Nugroho dari TC-AC-CS-246 (disubmit pada tanggal acuan `19/08/26`) dengan trial sumber SAMS Growth Active milik Client `Klinik Harapan Bunda+{runId}-152` (setara #71), dibuat lewat sesi API Fajar Nugroho hingga pengajuan tersimpan di hook `before`; term `[Subscription ID term 633 seed]` (Client `Apotek Sehat Sentosa+{runId}-152`, setara #90; SIEM, plan SIEM, Pending, 15/09/26 / 14/09/27, Plan Owner PT Maju Bersama (Distributor)) hasil approval milik aktor, dibuat lewat sesi API di hook `before` dan dibersihkan di hook `after` (S-06, S-12), Toggle `Require Approval for Allocation` ON dan aktor bukan bypass (#23), Duration awal `1`; Approval Timeout 3 hari (#26). General Settings Principal PT ABC (#28): Date Format `dd/MM/yy`, Time Format 24-hour, Timezone `Asia/Jakarta UTC+07:00` (tidak diubah spec).
- Jam: jam server dan jam browser diatur absolut lewat fixture waktu (tanggal acuan uji `19/08/26`), dan job sistem dipicu atau di-poll lewat kemampuan yang disediakan tim FE/BE (lihat suite.md). Jam dipulihkan di hook `after` dan sebelum membuka Changelog atau Subscription Log (S-09).
- Sesi API aktor: pelaku kedua dan pemicu state memakai sesi API dengan token yang tidak dihitung sebagai sesi web (lihat suite.md).
- Pemulihan state data milik spec yang diubah dilakukan fixture backend yang disediakan tim FE/BE sebagai langkah penghubung antar blok TC; state global yang dipulihkan hanya jam server dan jam browser (S-06).
- Acuan waktu (8b.3): T0 pengajuan TC-AC-CS-548 adalah waktu submit pengajuan seed, dibaca lewat API di hook `before`; T0 pengajuan TC-AC-CS-633 adalah waktu Save langkah 13, dibaca lewat API. Jam diatur ke `T0 + 3 hari + 1 menit` (Approval Timeout 3 hari, #26) dan tidak memakai tanggal literal. Risiko: margin 1 menit di bawah 5 menit rawan selisih antara T0 yang dibaca dan batas hitung job, serta selisih jam server dan jam browser; bila job tidak men-cancel pada margin itu, margin dinaikkan oleh tim FE/BE tanpa mengubah asersi.
- Baseline: jumlah entri Changelog, Activity Log, dan System Log serta jumlah email dan notifikasi yang relevan dicatat sebelum aksi pemicu pertama lewat kemampuan baca yang disediakan tim FE/BE (hook `before`); asersi entri baru memakai selisih terhadap baseline atau pencarian Subscription ID (S-12, R-11). Date atau Last Updated diasersi dengan toleransi satu menit dan jam server serta jam browser sinkron.
- Kelas harness d (job latar dan manipulasi jam). Spec ini satu jenis harness (jam server dan job sistem).
- Kemampuan teknis (disediakan tim FE/BE): picu satu siklus job Timeout Auto-Cancel dan kemampuan baca saldo Wallet (Reserve dilepas).
- State global yang diubah: jam server dan jam browser (dipulihkan di hook `after`, antar blok, dan sebelum membuka log); term seed yang berubah dipulihkan fixture backend antar blok.
- Hook `beforeEach` suite membuka Allocation > Client Subscription pada tab Current dan menjadi jaring pengaman `beforeunload` dan dialog `Unsaved Changes` (lihat suite.md).
- Guided Tooltip: hook suite before/after menyetel flag seen (lihat suite.md).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-548: Timeout Auto-Cancel pada term paid Waiting for Approval hasil Convert: trial tetap Active

1. Atur jam server dan jam browser ke `T0 + 3 hari + 1 menit` (T0 = waktu submit pengajuan seed; lewat batas timeout 3 hari), picu satu siklus job, dan poll hingga job selesai
2. Klik tab "History", ketik Search `Klinik Harapan Bunda+{runId}-152`, tekan Enter
3. Verifikasi term paid berstatus Canceled tanpa pelaku manusia
4. Verifikasi Reserve term paid dilepas
5. Klik `(←)` pada kotak Search, klik tab "Current", ketik Search `Klinik Harapan Bunda+{runId}-152`, tekan Enter
6. Verifikasi trial tetap Active dan tidak tersentuh
7. Klik ikon `⋯` pada baris trial
8. Verifikasi row action Convert masih tersedia
9. Tutup menu, pulihkan jam server dan jam browser ke jam normal, buka modal Changelog, ketik Search `Klinik Harapan Bunda+{runId}-152`, tekan Enter
10. Verifikasi entri baru Changelog mencatat Action `Timeout Auto-Cancel`, Field `Status`, Old `Waiting for Approval`, New `Canceled`, Modified By `System`
11. Tutup modal Changelog dengan `✕`, lalu pulihkan baseline pengajuan lewat fixture backend

### TC-AC-CS-633: Term Pending yang di-Edit kembali ke Waiting for Approval lalu Timeout Auto-Cancel menampilkan strip pada Start Date dan End Date

12. Ganti isi kotak search dengan `[Subscription ID term 633 seed]`, tekan Enter, lalu klik ikon `⋯` pada baris itu dan pilih `Edit`
13. Ubah Duration dari `1` menjadi `2`, klik `[Save]`, lalu catat waktu Save sebagai T0 (dibaca lewat API)
14. Verifikasi status term berubah dari Pending menjadi Waiting for Approval dengan SLA approval baru dihitung dari waktu Save
15. Atur jam server dan jam browser ke `T0 + 3 hari + 1 menit` (T0 = waktu Save langkah 13), picu satu siklus job, dan poll hingga job selesai
16. Klik `(←)` pada kotak Search, klik tab "History", ketik Search `[Subscription ID term 633 seed]`, tekan Enter
17. Verifikasi baris berstatus Canceled oleh Timeout Auto-Cancel tanpa pelaku manusia dan tampil di tab "History"
18. Verifikasi kolom Start Date dan End Date baris menampilkan "—" karena otorisasi sebelumnya tidak berlaku lagi setelah Edit (ACCS-LOGIC-01d)
19. Klik baris untuk membuka Subscription Detail
20. Verifikasi Subscription Detail menampilkan Start Date "—" dan End Date "—"
21. Pulihkan jam server dan jam browser ke jam normal dan baseline term lewat fixture backend

## Notes

- Langkah penghubung: tab, `(←)` pada kotak Search sebelum pindah tab (langkah 5 dan 16; kotak dikosongkan supaya Search berikutnya tidak bergantung pada status kotak sesudah pindah tab), Search (R-16: untuk menemukan baris target), penutupan modal dan menu, serta pemulihan jam dan baseline lewat fixture antar blok.
- Temuan untuk QA: (1) TC-AC-CS-548 bergantung pada TC-AC-CS-246 (Convert jalur request) dan tidak menyebut identitas pengajuan; spec men-seed pengajuan sendiri (S-06). (2) TC-AC-CS-548 butir a menyebut Reserve dilepas; cara cek tidak tertulis sehingga spec memakai kemampuan baca saldo Wallet. (3) TC-AC-CS-633 mencampur Edit (Save), pergeseran jam, dan asersi tampilan strip; spec mengikuti urutan TC.

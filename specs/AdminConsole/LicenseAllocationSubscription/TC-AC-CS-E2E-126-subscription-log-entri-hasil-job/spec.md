---
id: TC-AC-CS-E2E-126-subscription-log-entri-hasil-job
title: "Subscription Log: Entri Hasil Job"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-CS-602
  - TC-AC-CS-603
  - TC-AC-CS-604
coverage:
  web: automated
---

# Subscription Log: Entri Hasil Job

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal (Pre-setup #1) `totalControlSub_automated_{namaCompany}@qwertysystem.net` (`Hendra Wijaya`), password `Spectra.env.AC_SUB_TC_PASSWORD`; login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Email dan identitas data Pre-setup dirujuk lewat `Fixture.license-allocation-subscription` (belum ada; disediakan tim FE). Nama env var password adalah usulan: belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`, didaftarkan tim FE.
- Kelas harness d (objek uji: pencatatan hasil job sistem). Kemampuan teknis (disediakan tim FE/BE): atur jam server dan jam browser absolut (fixture waktu, tanggal acuan uji `19/08/26`); picu dan baca status job Timeout Auto-Cancel dan Scheduled Flip lewat kueri fixture status job (batas tunggu 2 menit); sesi API aktor.
- State dasar yang disiapkan di hook `before` lewat sesi API aktor (kolom Dependensi TC; endpoint tulis tidak tertulis di TC, PRD, atau LLD, lihat Temuan untuk QA), semua dirujuk lewat `Fixture.license-allocation-subscription`:
  1. TC-AC-CS-602: pengajuan Client `Toko Timeout+{runId}-126` FAMS Waiting for Approval dan pengajuan Trial Client `Toko Timeout+{runId}-126` SIEM Waiting for Approval yang akan melewati batas Approval Timeout 3 hari pada jam yang diatur langkah.
  2. TC-AC-CS-603: successor Pending Client `Toko Harapan Baru+{runId}-126` SAMS yang predecessor-nya sudah Archive (job flip melewati dan membatalkan successor).
  3. TC-AC-CS-604: term Pending Client `Percetakan Mega+{runId}-126` FAMS (setara #57) yang akan diaktifkan flip, dan Renew terjadwal Client `Toko Harapan Baru+{runId}-126` FAMS ke plan Professional (End Date `31/08/27`) yang diproses job Renew terjadwal.
- Satu kali jalan Scheduled Flip (langkah 19 sampai 22) memproses record TC-AC-CS-603 dan aktivasi `Percetakan Mega+{runId}-126` untuk TC-AC-CS-604; entri `Subscription renewed` TC-AC-CS-604 dihasilkan job Renew terjadwal yang dijalankan pada langkah 21 (kemampuan menjalankan job Renew terjadwal disediakan tim FE/BE, lihat Temuan untuk QA).
- Data milik spec: seed pada daftar di atas dibuat lewat API di hook `before`, bersuffix `+{runId}-126`, dan dibersihkan di hook `after` (S-06, S-12); tidak ada baris Pre-setup bersama yang ditulis spec ini.
- State global yang diubah: jam server dan jam browser digeser absolut; keduanya dipulihkan di langkah penghubung sebelum akun aktor membuka Subscription Log (S-09) dan di hook `after`. Jam adalah satu-satunya state global; seed lain dibersihkan di hook `after`.
- Hook suite (lihat `suite.md`): `beforeEach` membuka Allocation > Client Subscription tab Current dan menjadi jaring pengaman S-09; flag Guided Tooltip diatur `seen`. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-CS-602: Entri Subscription auto-canceled oleh Timeout Auto-Cancel tanpa pelaku

1. Atur jam server dan jam browser ke waktu absolut setelah batas Approval Timeout 3 hari pengajuan Client `Toko Timeout+{runId}-126`
2. Jalankan job Timeout Auto-Cancel dan tunggu job selesai (kueri fixture status job, batas 2 menit), catat waktu job
3. Pulihkan jam server dan jam browser
4. Klik tab `History`
5. Ketik Search `Toko Timeout+{runId}-126`, tekan Enter
6. Klik ikon `⋯` pada term `Toko Timeout+{runId}-126` FAMS yang dibatalkan job, klik `Subscription Log`
7. Verifikasi modal memuat entri teratas `Subscription auto-canceled`
8. Verifikasi entri teratas tanpa `by [PIC]`
9. Verifikasi baris Description entri teratas `Reason: Approval timeout`
10. Verifikasi Date & Time entri sesuai waktu job (toleransi satu menit)
11. Verifikasi tidak ada entri `Subscription canceled` oleh pelaku manusia
12. Klik `[✕]`
13. Klik ikon `⋯` pada baris Trial `Toko Timeout+{runId}-126` SIEM, klik `Subscription Log`
14. Verifikasi entri teratas `Subscription auto-canceled`
15. Verifikasi entri teratas tanpa `by [PIC]`
16. Verifikasi baris Description entri teratas `Reason: Approval timeout`
17. Verifikasi header `Status:` badge Canceled
18. Klik `[✕]`

### TC-AC-CS-603: Entri Subscription auto-canceled oleh Scheduled Flip Auto-Cancel memuat Reason predecessor

19. Atur jam server dan jam browser ke waktu absolut pada atau setelah Start Date successor Pending Client `Toko Harapan Baru+{runId}-126` SAMS
20. Jalankan job Scheduled Flip dan tunggu job selesai (kueri fixture status job, batas 2 menit), catat waktu job
21. Jalankan job Renew terjadwal untuk Renew Client `Toko Harapan Baru+{runId}-126` FAMS hingga tersimpan dan tunggu job selesai (kueri fixture status job, batas 2 menit), catat waktu job Renew
22. Pulihkan jam server dan jam browser
23. Ganti isi kotak search dengan `Toko Harapan Baru+{runId}-126`, tekan Enter
24. Klik ikon `⋯` pada successor Canceled `Toko Harapan Baru+{runId}-126` SAMS, klik `Subscription Log`
25. Verifikasi modal memuat entri teratas `Subscription auto-canceled`
26. Verifikasi entri teratas tanpa `by [PIC]`
27. Verifikasi baris Description entri teratas `Reason: Predecessor no longer Active, Expired, or Grace`
28. Verifikasi header `Status:` badge Canceled
29. Verifikasi tidak ada entri `Subscription activated`
30. Klik `[✕]`

### TC-AC-CS-604: Entri Subscription activated dan renewed oleh job tanpa pelaku

31. Klik tab `Current`
32. Ganti isi kotak search dengan `Percetakan Mega+{runId}-126`, tekan Enter
33. Klik ikon `⋯` pada term `Percetakan Mega+{runId}-126` FAMS yang diaktifkan flip, klik `Subscription Log`
34. Verifikasi entri teratas `Subscription activated`
35. Verifikasi entri teratas `Subscription activated` tanpa `by [PIC]`
36. Verifikasi entri teratas `Subscription activated` tanpa baris Description
37. Verifikasi header `Status:` badge Active
38. Verifikasi Date & Time entri sesuai waktu job Scheduled Flip (toleransi satu menit)
39. Klik `[✕]`
40. Ganti isi kotak search dengan `Toko Harapan Baru+{runId}-126`, tekan Enter
41. Klik ikon `⋯` pada term `Toko Harapan Baru+{runId}-126` FAMS hasil Renew terjadwal, klik `Subscription Log`
42. Verifikasi entri `Subscription renewed` tampil
43. Verifikasi entri `Subscription renewed` tanpa `by [PIC]`
44. Verifikasi baris Description entri `Subscription renewed` memuat `Plan: Professional`
45. Verifikasi baris Description entri `Subscription renewed` memuat `End Date: 31/08/27`
46. Verifikasi Date & Time entri sesuai waktu job Renew (toleransi satu menit)

## Notes

- Subjudul `###` memetakan langkah ke id TC granular. Ketiga TC memakai job sebagai objek uji (kelas d); tidak ada TC kelas lain di spec ini.
- Langkah penghubung (S-03): langkah 3 dan 22 (memulihkan jam sebelum membuka Subscription Log, S-09), langkah 4 dan 31 (pindah tab), langkah 5, 23, 32, 40 (Search untuk menemukan baris target, R-16), dan langkah 12, 18, 30, 39 (menutup modal).
- Satu jalan job Scheduled Flip (langkah 19 sampai 22) menjadi pemicu bersama TC-AC-CS-603 dan aktivasi `Percetakan Mega+{runId}-126` untuk TC-AC-CS-604 karena state dasar keduanya sudah disiapkan di hook `before` (`P-4`: dua TC kelas d berbagi state global jam dan job yang dibangun berurutan; hook suite memulihkan state sebelum spec). Job Renew terjadwal (langkah 21) dijalankan pada jam yang sama sebelum jam dipulihkan.
- Spec ini melewati ~35 langkah (46). Alasan: satu topik (entri Subscription Log hasil job sistem) dan satu permukaan, ketiga TC berbagi harness job dan jam yang sama sehingga pemecahan hanya menambah hook dan menggandakan pengaturan jam; kenaikan terutama dari pemecahan Verifikasi per klausa (S-01).
- Date & Time entri dibandingkan dengan waktu job yang dicatat sesudah job selesai, toleransi satu menit; jam server dan jam browser sinkron (S-12).
- Temuan untuk QA:
  - TC-AC-CS-602 Expected b dan TC-AC-CS-604 Expected c menyebut "PIC tercatat `System` di log"; nilai itu tidak tampil di judul entri sehingga tidak diasersi di UI.
  - Cara menjalankan job Timeout Auto-Cancel dan Scheduled Flip serta menyiapkan state dasar tidak tertulis di TC, PRD, atau LLD; ditulis sebagai kemampuan yang disediakan tim FE/BE tanpa endpoint karangan (S-13, R-19).
  - TC-AC-CS-604 (Expected untuk `Subscription renewed` pada `Toko Harapan Baru`) tidak menyebut job mana yang menghasilkan entri itu; sumber TC, PRD, dan LLD juga tidak menyebut bahwa Scheduled Flip yang memprosesnya. Spec menjalankan job Renew terjadwal (langkah 21, kemampuan disediakan tim FE/BE) sebagai asumsi; TC perlu menyebut job penghasil entri.
  - TC-AC-CS-602 tidak menyebut jam absolut yang dipakai; nilai disepakati tim FE/BE.
  - TC-AC-CS-602 langkah 1 menyebut term hasil job tanpa Subscription ID; spec memakai Search nama Client.

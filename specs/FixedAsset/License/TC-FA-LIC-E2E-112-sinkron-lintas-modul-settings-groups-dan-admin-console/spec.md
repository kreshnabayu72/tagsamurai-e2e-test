---
id: TC-FA-LIC-E2E-112-sinkron-lintas-modul-settings-groups-dan-admin-console
title: "Sinkron Lintas Modul: Settings Groups dan Admin Console Tercermin di Halaman License"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-412
  - TC-FA-LIC-413
  - TC-FA-LIC-414
  - TC-FA-LIC-415
  - TC-FA-LIC-416
coverage:
  web: automated
---

# Sinkron Lintas Modul: Settings Groups dan Admin Console Tercermin di Halaman License

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup dan penyetel state): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan kuota #12 (Remaining Kantor Pusat 200, Unmanaged 27, Total Asset License 5.000), riwayat #13 (4 term Subscription dan 7 alokasi). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` (pengecualian S-06: kuota dan riwayat Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: Total Asset License bertambah 500, term Subscription baru, jumlah Unmanaged berubah, dan entri baru bertambah permanen di Changelog Allocation Quota.
- Data Dinamis:
  - Grup anak Kantor Pusat `Divisi IT+{runId}-112` beralokasi 100 tanpa aset aktif, dibuat fixture BE (disediakan tim FE/BE; guard Delete grup Settings > Groups terpenuhi) di hook `before` dan dihapus spec pada TC-FA-LIC-412 (target hapus grup memakai grup milik spec, bukan grup Pre-setup). Karena grup ini ditambahkan di atas Pre-setup #12, nilai Allocated to Subgroups dan Remaining Kantor Pusat dicatat sebelum aksi (langkah 2) dan diasersi sebagai selisih. Penghapusan grup beralokasi menambah entri Remove Allocation permanen di Changelog Allocation Quota; hook `after` menghapus grup bila masih ada.
  - Grup level 1 `Cabang Bandung+{runId}-112`, dibuat spec pada TC-FA-LIC-413 dan dihapus di hook `after` (grup tanpa alokasi sehingga tidak menulis entri log).
- Kemampuan teknis:
  - Membaca jumlah entri Changelog Allocation Quota, jumlah baris Allocation History, dan jumlah baris Subscription History sebelum aksi (baseline) disediakan tim FE/BE.
  - Top-up Asset License dan Renew Subscription lewat fixture BE (langkah 22 dan 32), serta mengubah status aset ke dan dari Unmanaged lewat fixture BE (langkah 38); disediakan tim FE/BE, endpoint tidak dikarang.
  - Asersi absence push realtime didahului "Tunggu 5 detik tanpa memuat ulang halaman" (jendela standar pilihan spec, bukan nilai TC atau PRD).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-412: Hapus grup (cascade) menghapus baris alokasi: kuota kembali ke parent

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Buka License > Allocation Quota, klik node `Kantor Pusat`, catat Allocated to Subgroups dan Remaining Kantor Pusat
3. Buka Settings > Groups, ketik Search `Divisi IT+{runId}-112`, tekan Enter
4. Hapus grup `Divisi IT+{runId}-112` pada baris hasil Search
5. Tunggu aksi selesai
6. Buka License > Allocation Quota, klik node `Kantor Pusat`
7. Verifikasi Child Groups Quota menampilkan baris `Divisi Logistik` dan `Divisi Keuangan`
8. Verifikasi `Divisi IT+{runId}-112` tidak ada di Child Groups Quota
9. Verifikasi Kantor Pusat: Allocated to Subgroups berkurang `100` dari nilai pada langkah 2
10. Verifikasi Kantor Pusat: Remaining bertambah `100` dari nilai pada langkah 2
11. Klik ikon Changelog pada toolbar Child Groups Quota
12. Verifikasi jumlah entri Changelog bertambah tepat satu dari baseline
13. Verifikasi entri teratas Changelog (cascade-delete): Action `Remove Allocation`, Group Name `Divisi IT+{runId}-112`, Old Value `100`, New Value `—`
14. Tutup modal dengan `[×]`

### TC-FA-LIC-413: Grup level 1 baru di Settings Groups muncul sebagai Not Allocated

15. Buat grup level 1 `Cabang Bandung+{runId}-112` di Settings > Groups
16. Tunggu aksi selesai
17. Buka License > Allocation Quota, klik node `All Groups`
18. Verifikasi `Cabang Bandung+{runId}-112` muncul di Section 2 All Groups dengan Allocated Quota `—`
19. Verifikasi `Cabang Bandung+{runId}-112` muncul di Sidebar

### TC-FA-LIC-414: Top-up Asset License di Admin Console tercermin pada muat halaman berikutnya

20. Buka License > All License, catat nilai Total dan Remaining kolom `Asset`
21. Buka tab Allocation History, catat jumlah baris (baseline)
22. Lakukan top-up Asset License +500 lewat fixture BE hingga tersimpan
23. Tunggu 5 detik tanpa memuat ulang halaman
24. Verifikasi nilai Total kolom `Asset` tidak berubah dari nilai yang dicatat (tidak ada push realtime tanpa muat ulang)
25. Verifikasi nilai Remaining kolom `Asset` tidak berubah dari nilai yang dicatat
26. Muat ulang halaman License, buka All License
27. Verifikasi Total Asset License bertambah 500
28. Verifikasi Remaining bertambah 500
29. Buka tab Allocation History
30. Verifikasi Allocation History memuat satu baris alokasi baru dari baseline

### TC-FA-LIC-415: Add atau Renew Subscription di Admin Console tercermin pada Subscription History

31. Buka License > All License > Subscription History, catat jumlah baris (baseline)
32. Lakukan Renew Subscription lewat fixture BE hingga tersimpan
33. Tunggu aksi selesai
34. Muat ulang halaman License, buka Subscription History
35. Verifikasi baris term baru (Pending atau Active) bertambah satu dari baseline
36. Verifikasi urutan default Start Date terbaru

### TC-FA-LIC-416: Aset masuk atau keluar Unmanaged tercermin pada baris Unmanaged

37. Buka License > All License, catat nilai baris `Unmanaged`
38. Ubah status 2 aset menjadi Unmanaged lalu 1 aset kembali Active lewat fixture BE
39. Muat ulang halaman License, buka All License
40. Verifikasi baris `Unmanaged` bernilai 28 (27 + 2 − 1)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 2, 20, 21, 31, dan 37 mencatat baseline; langkah 3 mencari grup milik spec lewat Search sebelum Hapus (R-16, bagian 8b butir 13); langkah 14 menutup modal; langkah 5, 16, dan 33 menunggu aksi selesai sebelum berpindah surface (bagian 8b butir 8); langkah 23 menunggu jendela SSE sebelum asersi absence push realtime (bagian 6); langkah 26, 29, 34, dan 39 memuat ulang halaman dan berpindah tab.
- Absence pada langkah 8 didahului baris pembanding pada langkah 7 (bagian 8b butir 2); nilai tidak berubah pada langkah 24 dan 25 dibandingkan dengan nilai Total dan Remaining yang dicatat pada langkah 20.
- Temuan untuk QA:
  - TC-FA-LIC-412 butir b menyebut Allocated to Subgroups `500` dan Remaining `300` dengan target hapus `Divisi IT` Pre-setup; target hapus spec adalah grup milik spec yang ditambahkan di atas Pre-setup #12, sehingga spec mengasersi selisih `100` terhadap nilai yang dicatat pada langkah 2 (S-06).
  - TC-FA-LIC-414 butir b ("Allocation History memuat baris alokasi baru") tidak menyebut isi baris; spec mengasersi penambahan satu baris dari baseline.
  - TC-FA-LIC-415 butir a ("Pending atau Active") tidak menentukan status term baru; spec mengasersi baris term baru bertambah satu tanpa menentukan statusnya.
  - TC-FA-LIC-413 memakai nama literal `Cabang Bandung`; spec memberi suffix per run (S-12).
- Spec di atas 35 langkah (40 langkah): alasan semua blok satu topik (sinkron lintas modul Settings > Groups dan Admin Console) dan berdiri sendiri; langkah di atas 35 berasal dari pembuatan grup milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna.

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
- Data Pre-setup yang diubah spec: hierarki dan kuota #12 (Remaining Kantor Pusat 200, Unmanaged 27, Total Asset License 5.000), riwayat #13 (4 term Subscription dan 6 alokasi). Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` (pengecualian S-06: kuota dan riwayat Pre-setup tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: Total Asset License bertambah 500, term Subscription baru, jumlah Unmanaged berubah, dan entri baru bertambah permanen di Changelog Allocation Quota.
- Data Dinamis:
  - Grup anak Kantor Pusat `Divisi IT+{runId}-112` beralokasi 100 tanpa aset aktif, dibuat fixture BE (disediakan tim FE/BE; guard Delete grup Settings > Groups terpenuhi) di hook `before` dan dihapus spec pada TC-FA-LIC-412 (target hapus grup memakai grup milik spec, bukan grup Pre-setup). Karena grup ini ditambahkan di atas Pre-setup #12, nilai Allocated to Subgroups dan Remaining Kantor Pusat dicatat sebelum aksi (langkah 2) dan diasersi sebagai selisih. Penghapusan grup beralokasi menambah entri Remove Allocation permanen di Changelog Allocation Quota; hook `after` menghapus grup bila masih ada.
  - Grup level 1 `Cabang Bandung+{runId}-112`, dibuat spec pada TC-FA-LIC-413 dan dihapus di hook `after` (grup tanpa alokasi sehingga tidak menulis entri log).
- Kemampuan teknis:
  - Membaca jumlah entri Changelog Allocation Quota, jumlah baris Allocation History, dan jumlah baris Subscription History sebelum aksi (baseline) disediakan tim FE/BE.
  - Top-up Asset License dan Renew Subscription di Admin Console, serta mengubah status aset ke dan dari Unmanaged lewat fixture BE (pemicu sesuai PRD modul terkait, akun dan aksi disediakan tim FE/BE; endpoint tidak dikarang).
  - Asersi absence push realtime didahului "Tunggu 5 detik tanpa memuat ulang halaman" (jendela standar pilihan spec, bukan nilai TC atau PRD).
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-412: Hapus grup (cascade) menghapus baris alokasi: kuota kembali ke parent

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Buka License > Allocation Quota, klik node `Kantor Pusat`, catat Allocated to Subgroups dan Remaining Kantor Pusat
3. Hapus grup `Divisi IT+{runId}-112` di Settings > Groups
4. Tunggu aksi selesai
5. Buka License > Allocation Quota, klik node `Kantor Pusat`
6. Verifikasi Child Groups Quota menampilkan baris `Divisi Logistik` dan `Divisi Keuangan`
7. Verifikasi `Divisi IT+{runId}-112` tidak ada di Child Groups Quota
8. Verifikasi Kantor Pusat: Allocated to Subgroups berkurang `100` dari nilai pada langkah 2
9. Verifikasi Kantor Pusat: Remaining bertambah `100` dari nilai pada langkah 2
10. Klik ikon Changelog pada toolbar Child Groups Quota
11. Verifikasi Changelog bertambah satu entri baru dari baseline: Action `Remove Allocation`, Group Name `Divisi IT+{runId}-112`, Old Value `100`, New Value `—` (cascade-delete)
12. Tutup modal dengan `[×]`

### TC-FA-LIC-413: Grup level 1 baru di Settings Groups muncul sebagai Not Allocated

13. Buat grup level 1 `Cabang Bandung+{runId}-112` di Settings > Groups
14. Tunggu aksi selesai
15. Buka License > Allocation Quota, klik node `All Groups`
16. Verifikasi `Cabang Bandung+{runId}-112` muncul di Section 2 All Groups dengan Allocated Quota `—`
17. Verifikasi `Cabang Bandung+{runId}-112` muncul di Sidebar

### TC-FA-LIC-414: Top-up Asset License di Admin Console tercermin pada muat halaman berikutnya

18. Buka License > All License, catat nilai Total dan Remaining kolom `Asset`
19. Buka tab Allocation History, catat jumlah baris (baseline)
20. Lakukan top-up Asset License +500 di Admin Console
21. Tunggu 5 detik tanpa memuat ulang halaman
22. Verifikasi nilai Total dan Remaining kolom `Asset` tidak berubah dari nilai yang dicatat (tidak ada push realtime tanpa muat ulang)
23. Muat ulang halaman License, buka All License
24. Verifikasi Total Asset License bertambah 500
25. Verifikasi Remaining bertambah 500
26. Buka tab Allocation History
27. Verifikasi Allocation History memuat satu baris alokasi baru dari baseline

### TC-FA-LIC-415: Add atau Renew Subscription di Admin Console tercermin pada Subscription History

28. Buka License > All License > Subscription History, catat jumlah baris (baseline)
29. Renew Subscription di Admin Console
30. Muat ulang halaman License, buka Subscription History
31. Verifikasi baris term baru (Pending atau Active) bertambah satu dari baseline
32. Verifikasi urutan default Start Date terbaru

### TC-FA-LIC-416: Aset masuk atau keluar Unmanaged tercermin pada baris Unmanaged

33. Buka License > All License, catat nilai baris `Unmanaged`
34. Ubah status 2 aset menjadi Unmanaged lalu 1 aset kembali Active lewat fixture BE
35. Muat ulang halaman License, buka All License
36. Verifikasi baris `Unmanaged` bernilai 28 (27 + 2 − 1)

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1, 2, 18, 19, 28, dan 33 mencatat baseline; langkah 12 menutup modal; langkah 4 dan 14 menunggu aksi selesai sebelum berpindah surface (bagian 8b butir 8); langkah 21 menunggu jendela SSE sebelum asersi absence push realtime (bagian 6); langkah 23, 26, 30, dan 35 memuat ulang halaman dan berpindah tab.
- Absence pada langkah 7 didahului baris pembanding pada langkah 6 (bagian 8b butir 2); absence pada langkah 22 didahului nilai Total dan Remaining yang tampil pada langkah 18.
- Temuan untuk QA:
  - TC-FA-LIC-412 butir b menyebut Allocated to Subgroups `500` dan Remaining `300` dengan target hapus `Divisi IT` Pre-setup; target hapus kini grup milik spec yang ditambahkan di atas Pre-setup #12, sehingga spec mengasersi selisih `100` terhadap nilai yang dicatat pada langkah 2 (S-06).
  - TC-FA-LIC-414 butir b ("Allocation History memuat baris alokasi baru") tidak menyebut isi baris; spec mengasersi penambahan satu baris dari baseline.
  - TC-FA-LIC-415 butir a ("Pending atau Active") tidak menentukan status term baru; spec mengasersi baris term baru bertambah satu tanpa menentukan statusnya.
  - TC-FA-LIC-413, 414, 415, dan 416 tidak menyebut akun Admin Console untuk top-up, Renew Subscription, dan perubahan status aset; spec menuliskannya sebagai kemampuan yang disediakan tim FE/BE.
  - TC-FA-LIC-413 memakai nama literal `Cabang Bandung`; spec memberi suffix per run (S-12).
- Alasan di atas 35 langkah (36 langkah): semua blok satu topik (sinkron lintas modul Settings > Groups dan Admin Console) dan berdiri sendiri; langkah di atas 35 berasal dari pembuatan grup milik spec; kegagalan satu blok tidak membuat blok lain kehilangan makna.

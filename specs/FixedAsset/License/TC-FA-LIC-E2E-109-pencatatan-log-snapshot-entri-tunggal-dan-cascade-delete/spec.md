---
id: TC-FA-LIC-E2E-109-pencatatan-log-snapshot-entri-tunggal-dan-cascade-delete
title: "Pencatatan Log: Snapshot Immutability, Snapshot Nama Grup, dan Satu Aksi Satu Entri per Surface"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-379
  - TC-FA-LIC-380
  - TC-FA-LIC-381
coverage:
  web: automated
---

# Pencatatan Log: Snapshot Immutability, Snapshot Nama Grup, dan Satu Aksi Satu Entri per Surface

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Pre-setup yang diubah spec: hierarki dan alokasi grup #12 (Divisi Logistik beralokasi 500 dalam Kantor Pusat) pada blok TC-FA-LIC-379 dan TC-FA-LIC-381. Pemulihan oleh fixture BE pemulih (disediakan tim FE/BE) di hook `before` dan `after` serta pada langkah 9 dan 22 antar blok TC (pengecualian S-06: alokasi grup Pre-setup bernama literal tidak dapat dimiliki spec, suite berjalan serial). Efek yang dicatat: kolom Last Updated alokasi Divisi Logistik berubah dan entri baru bertambah permanen di Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset.
- Data Dinamis (blok TC-FA-LIC-380, rename grup memakai grup milik spec, bukan grup Pre-setup): grup anak Kantor Pusat `Divisi Logistik+{runId}-109` tanpa alokasi dan tanpa aset aktif, dibuat fixture BE (disediakan tim FE/BE) di hook `before`; nama hasil rename `Divisi Logistik Pusat+{runId}-109`. Fixture di langkah 22 dan hook `after` memulihkan grup ke nama `Divisi Logistik+{runId}-109` tanpa alokasi atau menghapusnya; penghapusan grup beralokasi menambah entri Remove Allocation permanen di tiga surface.
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log sebelum aksi (baseline, langkah 1 dan 23) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline.
- Jalur menu: System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log; rename grup lewat Settings > Groups.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-379: Snapshot immutability: edit dua kali, entri pertama tidak berubah

1. Catat jumlah entri Changelog Allocation Quota (baseline)
2. Buka tab Allocation Quota, klik node `Kantor Pusat`
3. Klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
4. Klik `[Edit]` pada `Divisi Logistik`, isi `650`, klik `[Save]`
5. Klik ikon Changelog pada toolbar Child Groups Quota
6. Verifikasi entri pertama (lebih lama), dicari lewat Group Name `Divisi Logistik`, Field `Allocated Quota`, dan Old Value `500`, tetap New Value `600`
7. Verifikasi entri kedua (lebih baru dari entri pertama), dicari lewat Group Name `Divisi Logistik`, Field `Allocated Quota`, dan Old Value `600`, New Value `650`
8. Verifikasi jumlah entri bertambah tepat dua dari baseline (tidak ada entri yang ditimpa)

### TC-FA-LIC-380: Snapshot nama grup: rename grup tidak mengubah entri lama

9. Tutup modal dengan `[×]`, lalu pulihkan Pre-setup #12 lewat fixture BE
10. Klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik+{runId}-109`, isi `50`, klik `[Save]`
11. Tunggu aksi selesai
12. Rename `Divisi Logistik+{runId}-109` menjadi `Divisi Logistik Pusat+{runId}-109` di Settings > Groups
13. Tunggu aksi selesai
14. Buka License > Allocation Quota, klik node `All Groups`, klik ikon Changelog pada toolbar Level 1 Groups Quota
15. Verifikasi entri lama, dicari lewat Field `Allocated Quota`, Old Value `—`, dan New Value `50`, tetap Group Name `Divisi Logistik+{runId}-109`
16. Tutup modal dengan `[×]`, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik Pusat+{runId}-109`, isi `60`, klik `[Save]`
17. Klik ikon Changelog pada toolbar Child Groups Quota
18. Verifikasi entri baru, dicari lewat Field `Allocated Quota`, Old Value `50`, dan New Value `60`, memakai Group Name `Divisi Logistik Pusat+{runId}-109`
19. Buka Filter Panel, buka dropdown `Group Name`
20. Verifikasi opsi Group Name memuat kedua nama `Divisi Logistik+{runId}-109` dan `Divisi Logistik Pusat+{runId}-109` sebagai snapshot historis
21. Tutup dropdown, tutup modal dengan `[×]`

### TC-FA-LIC-381: Satu aksi menghasilkan tepat satu entri per surface

22. Pulihkan Pre-setup #12 lewat fixture BE (grup milik spec kembali ke nama `Divisi Logistik+{runId}-109` tanpa alokasi)
23. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log (baseline)
24. Buka License > Allocation Quota, klik node `Kantor Pusat`, klik `[Edit]` pada `Divisi Logistik`, isi `600`, klik `[Save]`
25. Klik ikon Changelog pada toolbar Child Groups Quota
26. Verifikasi entri baru Divisi Logistik tampil di Changelog dan jumlah entri bertambah tepat satu dari baseline
27. Verifikasi tidak ada entri baru di Changelog untuk Kantor Pusat, Divisi IT, atau grup lain
28. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
29. Verifikasi entri baru Divisi Logistik tampil di System Log dan jumlah entri bertambah tepat satu dari baseline
30. Verifikasi tidak ada entri baru di System Log untuk Kantor Pusat, Divisi IT, atau grup lain
31. Buka Fixed Asset > Reports & Logs > Activity Log
32. Verifikasi entri baru Divisi Logistik tampil di Activity Log dan jumlah entri bertambah tepat satu dari baseline
33. Verifikasi tidak ada entri baru di Activity Log untuk Kantor Pusat, Divisi IT, atau grup lain

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 23 mencatat baseline; langkah 9, 21, dan 22 menutup modal dan memulihkan Pre-setup #12 antar blok (S-09); langkah 10 mengalokasikan grup milik spec sebagai sumber entri lama untuk TC-FA-LIC-380; langkah 11 dan 13 menunggu aksi selesai sebelum berpindah surface (bagian 8b butir 8); langkah 14 membuka Changelog pada node `All Groups`; langkah 16 menutup modal sebelum edit alokasi grup hasil rename (TC-FA-LIC-380 langkah 3).
- Entri hasil aksi dicari lewat Group Name, Field, Old Value, dan New Value, bukan posisi teratas (S-12): entri bercap waktu masa depan dari spec lain dapat berada di atas entri baru.
- Absence di langkah 27, 30, dan 33 didahului `Verifikasi` entri baru milik Divisi Logistik pada surface yang sama (langkah 26, 29, dan 32) sebagai anchor positif (bagian 8b butir 2).
- Cascade-delete grup beralokasi (TC-FA-LIC-382 dan TC-FA-LIC-602) ada di spec `TC-FA-LIC-E2E-143`.
- Temuan untuk QA:
  - TC-FA-LIC-380 langkah 4 meminta "Buka Filter Panel dan buka opsi `Group Name`" tanpa menyebut modal yang dipakai; spec memakai modal yang sama dengan langkah 17.
  - TC-FA-LIC-381 butir b ("tidak ada entri untuk Kantor Pusat, Divisi IT, atau grup lain") tidak menyebut surface; spec mengasersinya pada ketiga surface.
  - TC-FA-LIC-380 me-rename `Divisi Logistik` Pre-setup dengan prasyarat entri lama (29/09/26 10:05) dari Pre-setup #27; rename grup bernama literal tidak dapat dimiliki spec (S-06). Spec me-rename grup milik spec bersuffix, membuat entri lama sendiri lewat alokasi `50` (Old Value `—`) lalu mengedit ke `60`, bukan `500` dan `620`, karena Remaining Kantor Pusat 200 tidak cukup untuk 500; Date entri lama tidak diasersi.

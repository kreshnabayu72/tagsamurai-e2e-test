---
id: TC-FA-LIC-E2E-143-pencatatan-log-cascade-delete-grup-beralokasi
title: "Pencatatan Log Cascade-Delete Grup Beralokasi di Changelog, System Log Admin, dan Activity Log"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-382
  - TC-FA-LIC-602
coverage:
  web: automated
---

# Pencatatan Log Cascade-Delete Grup Beralokasi di Changelog, System Log Admin, dan Activity Log

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Pre-setup #1) `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` (Rudi Hartono, admin penghapus grup), client PT Sejahtera plan Paid (`License allocation per group` ON, General Settings `dd/MM/yy`, `HH:mm`, `Asia/Jakarta`), password dari `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env `FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`.
- Hook suite (sesi API aktor, fixture BE pemulih Pre-setup, jam dan format tanggal): dinyatakan sekali di `suite.md`; spec ini merujuknya.
- Data Dinamis yang dihapus spec (grup milik spec bersuffix, bukan grup Pre-setup #12), dibuat fixture BE (disediakan tim FE/BE; tanpa aset aktif sehingga guard Delete grup Settings > Groups terpenuhi; kuota induk disesuaikan fixture) di hook `before` untuk blok TC-FA-LIC-382 dan pada langkah 13 untuk blok TC-FA-LIC-602:
  - Blok TC-FA-LIC-382: grup anak Kantor Pusat `Divisi IT+{runId}-143` beralokasi 100.
  - Blok TC-FA-LIC-602: grup anak Kantor Pusat `Divisi Logistik+{runId}-143` beralokasi 500 dengan child `Gudang A+{runId}-143` beralokasi 100.
  Hook `after` menghapus grup milik spec yang tersisa. Efek yang dicatat: grup dihapus dari hierarki, kuota kembali ke parent, dan entri baru bertambah permanen di Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log Fixed Asset.
- Kemampuan teknis: membaca jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log sebelum aksi (baseline, langkah 1 dan 14) disediakan tim FE/BE; asersi jumlah memakai selisih terhadap baseline.
- Jalur menu: hapus grup lewat Settings > Groups; System Log lewat Global Settings > User > Detail Rudi Hartono > Tab System Log; Activity Log lewat Fixed Asset > Reports & Logs > Activity Log.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-LIC-382: Cascade-delete grup beralokasi menulis entri Remove Allocation

1. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log (baseline)
2. Hapus grup `Divisi IT+{runId}-143` dari Settings > Groups
3. Tunggu aksi selesai
4. Buka License > Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
5. Verifikasi Changelog bertambah tepat satu entri dari baseline
6. Verifikasi entri baru, dicari lewat Group Name `Divisi IT+{runId}-143`, Field `Allocated Quota`, Old Value `100`, dan New Value `—`: Action `Remove Allocation`, Modified By `Rudi H`
7. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
8. Verifikasi System Log bertambah tepat satu entri dari baseline
9. Verifikasi entri baru System Log, dicari lewat Name `Divisi IT+{runId}-143`, Field `Allocated Quota`, Old Value `100`, dan New Value `—`: Action `Remove Allocation`, Object `License`
10. Buka Fixed Asset > Reports & Logs > Activity Log
11. Verifikasi Activity Log bertambah tepat satu entri dari baseline
12. Verifikasi entri baru Activity Log, dicari lewat Name `Divisi IT+{runId}-143`, Field `Allocated Quota`, Old Value `100`, dan New Value `—`: Action `Remove Allocation`, Object `License`, Modified By `Rudi H`

### TC-FA-LIC-602: Cascade-delete grup beralokasi dengan child beralokasi: satu entri per grup

13. Siapkan lewat fixture BE grup milik spec `Divisi Logistik+{runId}-143` beralokasi 500 dan child `Gudang A+{runId}-143` beralokasi 100, keduanya tanpa aset aktif
14. Catat jumlah entri Changelog Allocation Quota, System Log Rudi Hartono, dan Activity Log (baseline)
15. Hapus grup `Divisi Logistik+{runId}-143` dari Settings > Groups
16. Tunggu aksi selesai
17. Buka License > Allocation Quota, klik ikon Changelog pada toolbar Level 1 Groups Quota
18. Verifikasi Changelog memuat dua entri baru: Action `Remove Allocation`, Group Name `Divisi Logistik+{runId}-143`, Field `Allocated Quota`, Old Value `500`, New Value `—`, Modified By `Rudi H`; dan Action `Remove Allocation`, Group Name `Gudang A+{runId}-143`, Field `Allocated Quota`, Old Value `100`, New Value `—`, Modified By `Rudi H`
19. Verifikasi Changelog bertambah tepat dua entri (satu per grup beralokasi yang terhapus)
20. Tutup modal dengan `[×]`, lalu buka Global Settings > User > Detail Rudi Hartono > Tab System Log
21. Verifikasi System Log memuat dua entri baru: Action `Remove Allocation`, Object `License`, Field `Allocated Quota`, Name `Divisi Logistik+{runId}-143` (Old Value `500`, New Value `—`) dan Name `Gudang A+{runId}-143` (Old Value `100`, New Value `—`)
22. Verifikasi System Log bertambah tepat dua entri
23. Buka Fixed Asset > Reports & Logs > Activity Log
24. Verifikasi Activity Log memuat dua entri baru: Action `Remove Allocation`, Object `License`, Field `Allocated Quota`, Name `Divisi Logistik+{runId}-143` (Old Value `500`, New Value `—`) dan Name `Gudang A+{runId}-143` (Old Value `100`, New Value `—`), Modified By `Rudi H`
25. Verifikasi Activity Log bertambah tepat dua entri

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC.
- Langkah penghubung (tanpa `Verifikasi`): langkah 1 dan 14 mencatat baseline; langkah 3 dan 16 menunggu aksi selesai sebelum berpindah surface (bagian 8b butir 8); langkah 7, 10, 13, 20, dan 23 berpindah surface atau menyiapkan data milik spec antar blok (S-09). Aksi menghapus grup berada di akhir tiap blok sebagai aksi uji (S-10).
- Entri hasil aksi dicari lewat Group Name atau Name, Field, Old Value, dan New Value, bukan posisi teratas (S-12): entri bercap waktu masa depan dari spec lain dapat berada di atas entri baru. Field `Allocated Quota` pada langkah 6, 9, dan 12 melengkapi identifikasi entri dan sesuai TC-FA-LIC-382 butir a, c, dan d.
- Grup yang dihapus adalah grup milik spec bersuffix `{runId}-143` yang menggantikan `Divisi IT`, `Divisi Logistik`, dan `Gudang A` Pre-setup #12 sebagai target hapus (S-06 `[KEPUTUSAN 2026-11-02]`); TC-FA-LIC-382 dan TC-FA-LIC-602 menyebut nama literal Pre-setup.
- Temuan untuk QA:
  - TC-FA-LIC-382 butir b ("entri ditulis dalam transaksi yang sama dengan Delete grup; tidak ada entri tertinggal bila Delete gagal") tidak dapat diamati dari UI dan TC tidak memberi langkah pengamatan; spec tidak mengasersinya (Catatan TC menyatakan atomisitas tidak di-assert pada TC UI).
  - TC-FA-LIC-382 butir a menulis Modified By "nama admin yang menghapus grup" dan butir d `Rudi H`; spec memakai `Rudi H` (admin penghapus adalah aktor Pre-setup #1).

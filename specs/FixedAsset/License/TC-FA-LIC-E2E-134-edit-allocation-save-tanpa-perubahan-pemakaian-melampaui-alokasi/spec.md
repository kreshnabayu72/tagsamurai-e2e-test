---
id: TC-FA-LIC-E2E-134-edit-allocation-save-tanpa-perubahan-pemakaian-melampaui-alokasi
title: "Edit Allocation: Save Tanpa Perubahan pada Grup yang Pemakaiannya Melampaui Allocated Quota"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-FA-LIC-598
coverage:
  web: automated
---

# Edit Allocation: Save Tanpa Perubahan pada Grup yang Pemakaiannya Melampaui Allocated Quota

## Prerequisites

- Mode: FE+BE.
- Role yang diuji / akun aktor:

| Kode | Role | Email | Env var password |
|---|---|---|---|
| Pre-setup #1 | Total Control (Rudi Hartono) | `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |

- Login di hook `before` spec ini (Total Control, Pre-setup #1); halaman Fixed Asset > License dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control, Pre-setup #1).
- Password tidak ditulis di spec atau fixture; `Spectra.env.FA_TC_PASSWORD` didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example` (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-license` untuk akun aktor disetel true oleh hook `before` suite dan dipulihkan hook `after` suite (dinyatakan di `suite.md`).
- Suite berjalan serial (`parallel: false`): hierarki dan alokasi grup dipakai bersama dan diubah spec ini; hook `after` memulihkannya.
- Data: Pre-setup #12 dengan Divisi IT beralokasi 100, Used by This Group 110, Reserved by This Group 0, tanpa subgroup (pemakaian melampaui alokasi), sehingga Minimum Quota 110; diatur fixture BE penyetel pada langkah yang disebut.
- Pengecualian S-06 `[KEPUTUSAN 2026-10-30]`: target aksi tulis adalah grup Pre-setup #12 bernama literal karena hierarki dan kuotanya tidak dapat dimiliki spec (nama, urutan, dan nilai kuota menjadi objek asersi). Pemulihan ke Pre-setup #12 dijamin fixture BE pemulih yang disediakan tim FE/BE (dinyatakan di `suite.md`), dijalankan di hook `before` dan `after` serta sebagai langkah penghubung antar blok. Efek: Last Updated baris alokasi, entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log bertambah. Fixture `Fixture.fixedAssetLicense` belum ada dan disediakan tim FE.
- Kemampuan teknis: Intercept jaringan mengamati respons permintaan Save (status).
- Kemampuan teknis: Kemampuan membaca jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline (disediakan tim FE/BE; audit trail permanen sehingga asersi memakai selisih jumlah entri, S-12). Modified By tidak diasersi.

## Test Steps

### TC-FA-LIC-598: Save tanpa perubahan nilai pada grup yang pemakaiannya melampaui Allocated Quota

1. Jalankan fixture BE pemulih Pre-setup #12 dan penyetel Divisi IT (beralokasi 100, Used 110, Reserved 0) hingga tersimpan
2. Muat ulang halaman License, lalu klik tab `Allocation Quota`
3. Klik node `Kantor Pusat` di Sidebar
4. Catat jumlah entri `Changelog: Allocation Quota`, System Log aktor, dan Activity Log sebagai baseline
5. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
6. Klik field `New Allocated Quota`, lalu pindahkan fokus keluar dari field (blur) tanpa mengubah isi
7. Verifikasi field New Allocated Quota ber-pre-fill `100`
8. Verifikasi tidak ada pesan V-FALIC-01
9. Klik `[Save]` sambil mengamati respons permintaan pada intercept jaringan
10. Verifikasi modal tertutup
11. Verifikasi toast netral `No changes to save.` (bukan toast sukses)
12. Verifikasi respons permintaan `200 OK`
13. Verifikasi Allocated Quota baris `Divisi IT` tetap `100`
14. Periksa `Changelog: Allocation Quota` (ikon Changelog pada toolbar), System Log aktor, dan Activity Log
15. Verifikasi entri lama yang sudah ada sebelum aksi tampil di `Changelog: Allocation Quota`, System Log aktor, dan Activity Log
16. Verifikasi tidak ada entri baru di `Changelog: Allocation Quota`, System Log aktor, dan Activity Log (jumlah entri sama dengan baseline)
17. Tutup modal `Changelog: Allocation Quota`
18. Klik tombol ikon `[Edit]` pada baris `Divisi IT`
19. Ubah nilai menjadi `105`
20. Pindahkan fokus keluar dari field (blur)
21. Verifikasi pesan inline V-FALIC-01 tampil: `Cannot set quota below used, reserved, and subgroup-allocated quota (110).`
22. Klik icon `[×]`
23. Verifikasi dialog `Unsaved Changes` dengan teks `You have unsaved changes. Are you sure you want to leave?` dan tombol `[Cancel]` dan `[Leave]`
24. Klik `[Leave]`

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah penghubung (S-03): fixture BE pemulih dan penyetel, muat ulang halaman, dan klik tab menyiapkan state; `Periksa ...` membuka surface log untuk membaca jumlah entri; menutup modal Changelog dan modal dirty (`[×]`, dialog `Unsaved Changes`, `[Leave]`, S-08).
- Anchor absence entri log: toast netral `No changes to save.` (langkah 11), baseline jumlah entri dicatat sebelum aksi (langkah 4), dan entri lama tampil di ketiga surface (langkah 15) sebelum asersi jumlah entri sama dengan baseline (langkah 16) (S-12, bagian 8b butir 2).
- Asersi "tidak ada entri baru" pada langkah 16 berupa asersi jumlah dengan baseline langkah 4 (jumlah entri sama), bukan asersi absence kelas g (bagian 3 prinsip 13g, S-12).
- Temuan untuk QA:
  - TC-FA-LIC-598: klausa `nol entri baru` di tiga surface log ditulis di spec ini dengan baseline; belum ada spec absence (kelas g) yang memuat aksi nyata untuk TC ini (S-05).

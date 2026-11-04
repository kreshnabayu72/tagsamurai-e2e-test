---
id: TC-FA-LIC-E2E-150-allocation-history-ceklis-dan-unceklis-per-kolom-setup-column
title: "Allocation History: Setup Column Ceklis dan Unceklis per Kolom Hideable Visible Default"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-251
coverage:
  web: automated
---
# Allocation History: Setup Column Ceklis dan Unceklis per Kolom Hideable Visible Default

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): enam alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001 (urutan default Last Updated terbaru lebih dulu; Plan Owner seluruhnya PT Maju Bersama (Distributor); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001).
- Pemulihan konfigurasi kolom: konfigurasi Setup Column yang disimpan spec ini didaftarkan di `suite.md`; hook `after` menghapus preferensi kolom di browser (bukan `[Reset to Default]`; kemampuan disediakan tim FE).
- Daftar kolom Hideable Visible default (parameter langkah 2 sampai 12): `Allocation ID`, `Subscription ID`, `License Type`, `Quantity`, `Status`, `Date`, `End Date`, `Plan Owner`, `Last Updated` (sembilan kolom).
- State yang diubah dan dipulihkan: visibilitas kolom Setup Column (setiap iterasi memulihkannya pada langkah 12; didaftarkan di `suite.md`).

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-251: Ceklis dan unceklis per kolom

Untuk setiap kolom pada daftar kolom (langkah 2 sampai 12):

2. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
3. Hilangkan centang kolom
4. Verifikasi kolom hilang dari Live Preview
5. Klik `[Save]`
6. Verifikasi kolom hilang dari tabel
7. Muat ulang halaman (F5), lalu klik sub-tab `Allocation History`
8. Verifikasi kolom tetap hilang dari tabel
9. Klik header kolom Actions `⋯`, lalu klik `Setup Column...`
10. Centang kembali kolom
11. Verifikasi kolom kembali tampil di Live Preview
12. Klik `[Save]`

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah setelah ekspansi (12 langkah nominal; 100 langkah setelah ekspansi sembilan iterasi). Alasan: satu TC, satu topik (Setup Column Allocation History), satu dataset Pre-setup #13 yang hanya dibaca, dan langkah 2 sampai 12 diulang per kolom dengan parameter di daftar kolom `## Prerequisites`, tanpa langkah bersyarat dan dengan satu `Verifikasi` per klausa (S-01); satu TC tidak dapat dibagi ke spec lain.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 1 (klik sub-tab sebagai aksi deterministik), langkah 7 (klik sub-tab sesudah muat ulang agar sub-tab aktif deterministik), dan langkah 12 (memulihkan kolom; S-09, butir 14 bagian 8b).
- Temuan untuk QA:
  - TC-FA-LIC-251 menulis "tampilkan kembali" tanpa menyebut `Verifikasi` tabel setelah `[Save]` ulang; spec mengasersi kembali tampil di Live Preview (Expected TC: "kembali tampil saat dicentang ulang") dan menyimpan ulang sebagai pemulihan.
  - TC-FA-LIC-251 tidak menyebut Post Condition (`-`); tidak ada yang diasersi.

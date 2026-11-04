---
id: TC-FA-LIC-E2E-138-subscription-history-sort-siklus-3-state-per-kelas-kolom
title: "Subscription History: Sort Siklus 3 State per Kelas Kolom (Alfabetis dan Tanggal)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-195
  - TC-FA-LIC-196
coverage:
  web: automated
---
# Subscription History: Sort Siklus 3 State per Kelas Kolom (Alfabetis dan Tanggal)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Subscription History, hanya dibaca): empat term Subscription lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): SUBS-20270101-00001 (Plan Professional, Type Paid, Status Pending, Plan Owner PT Maju Bersama (Distributor)), SUBS-20260101-00001 (Professional, Paid, Active, PT Maju Bersama (Distributor)), SUBS-20250101-00001 (Professional, Paid, Renewed, PT Maju Bersama (Distributor)), SUBS-20241201-00001 (Enterprise, Trial, Converted, PT ABC (Principal)). Urutan default Start Date terbaru lebih dulu: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001.
- Alias baris untuk tabel urutan: S1 = SUBS-20270101-00001, S2 = SUBS-20260101-00001, S3 = SUBS-20250101-00001, S4 = SUBS-20241201-00001. Urutan default (netral): S1, S2, S3, S4.
- Anggota sort per kelas kolom (parameter langkah 2 sampai 7):

  | TC | Kolom | Klik 1 (Ascending) | Klik 2 (Descending) |
  |---|---|---|---|
  | TC-FA-LIC-195 | Subscription ID | S4, S3, S2, S1 | S1, S2, S3, S4 |
  | TC-FA-LIC-195 | Plan | S4, S1, S2, S3 | S1, S2, S3, S4 |
  | TC-FA-LIC-195 | Type | S1, S2, S3, S4 | S4, S1, S2, S3 |
  | TC-FA-LIC-195 | Status | S2, S4, S1, S3 | S3, S1, S4, S2 |
  | TC-FA-LIC-195 | Plan Owner | S4, S1, S2, S3 | S1, S2, S3, S4 |
  | TC-FA-LIC-196 | Start Date | S4, S3, S2, S1 | S1, S2, S3, S4 |
  | TC-FA-LIC-196 | End Date | S4, S3, S2, S1 | S1, S2, S3, S4 |

- State yang diubah: Sort kolom tiap anggota; klik ketiga menetralkannya kembali sehingga tidak perlu pemulihan lain.

## Test Steps

1. Klik sub-tab `Subscription History`

### TC-FA-LIC-195 dan TC-FA-LIC-196: Siklus sort Ascending, Descending, netral

Untuk setiap baris tabel "Anggota sort per kelas kolom" (langkah 2 sampai 7):

2. Klik header kolom baris tabel sekali (Ascending)
3. Verifikasi indikator `↑` dan urutan baris sesuai kolom `Klik 1 (Ascending)` baris tabel
4. Klik header kolom baris tabel sekali lagi (Descending)
5. Verifikasi indikator `↓` dan urutan baris sesuai kolom `Klik 2 (Descending)` baris tabel
6. Klik header kolom baris tabel sekali lagi (netral)
7. Verifikasi urutan baris kembali ke urutan default: SUBS-20270101-00001, SUBS-20260101-00001, SUBS-20250101-00001, SUBS-20241201-00001

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (7 langkah nominal; 43 langkah setelah ekspansi). Alasan: langkah 2 sampai 7 diulang per kolom (tujuh iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat, dan tiap iterasi memuat satu `Verifikasi` per klausa Expected TC (S-01); semua iterasi satu topik (siklus sort), satu dataset Pre-setup #13 yang hanya dibaca, dan berdiri sendiri.
- TC-FA-LIC-195 dan TC-FA-LIC-196 digabung dalam satu blok ulang karena langkah ujinya identik; tabel Prerequisites memetakan baris ke id TC. Langkah 1 (klik sub-tab sebagai aksi deterministik) adalah langkah penghubung.
- Temuan untuk QA: TC-FA-LIC-195 dan TC-FA-LIC-196 tidak menyebut Post Condition (`-`); tidak ada yang diasersi. Urutan seri pada kolom dengan nilai sama (mis. Type Paid: S1, S2, S3) mengikuti Expected TC.

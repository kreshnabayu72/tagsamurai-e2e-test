---
id: TC-FA-LIC-E2E-137-allocation-history-sort-siklus-3-state-per-kelas-kolom
title: "Allocation History: Sort Siklus 3 State per Kelas Kolom (Alfabetis, Numerik, dan Tanggal)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-LIC-236
  - TC-FA-LIC-237
  - TC-FA-LIC-238
coverage:
  web: automated
---
# Allocation History: Sort Siklus 3 State per Kelas Kolom (Alfabetis, Numerik, dan Tanggal)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Pre-setup #1 (`Fixture.fixedAssetLicense.akunTotalControl`; pola email `totalControlFixedAsset_automated_{namaCompany}@qwertysystem.net`), kredensial `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite. Spec tidak mengganti akun. Password tidak ditulis di spec atau fixture.
- Guided Tooltip: flag seen diatur dan dipulihkan hook suite (dinyatakan sekali di `suite.md`).
- Data Pre-setup #13 (Allocation History, hanya dibaca): tujuh alokasi lewat `Fixture.fixedAssetLicense.riwayat` (fixture belum ada; disediakan tim FE/BE): LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001, LALC-20241205-00001 (urutan default Last Updated terbaru lebih dulu; enam alokasi pertama ber-Plan Owner PT Maju Bersama (Distributor), LALC-20241205-00001 ber-Plan Owner PT ABC (Principal); LALC-20250210-00001 berstatus Expired, SUBS-20250101-00001; LALC-20241205-00001 `Addon (Audit)` berstatus Expired, SUBS-20241201-00001; Quantity LALC-20260101-00001 = 3000 dan LALC-20260312-00002 = +1500).
- Alias baris untuk tabel urutan: R1 = LALC-20260801-00004, R2 = LALC-20260720-00003, R3 = LALC-20260515-00002, R4 = LALC-20260312-00002, R5 = LALC-20260101-00001, R6 = LALC-20250210-00001, R7 = LALC-20241205-00001. Urutan default (netral, Last Updated terbaru lebih dulu): R1, R2, R3, R4, R5, R6, R7.
- Anggota sort per kelas kolom (parameter langkah 2 sampai 7):

  | TC | Kolom | Klik 1 (Ascending) | Klik 2 (Descending) |
  |---|---|---|---|
  | TC-FA-LIC-236 | Allocation ID | R7, R6, R5, R4, R3, R2, R1 | R1, R2, R3, R4, R5, R6, R7 |
  | TC-FA-LIC-236 | Subscription ID | R7, R6, R1, R2, R3, R4, R5 | R1, R2, R3, R4, R5, R6, R7 |
  | TC-FA-LIC-236 | License Type | R3, R7, R1, R2, R4, R5, R6 | R2, R4, R5, R6, R1, R3, R7 |
  | TC-FA-LIC-236 | Status | R1, R2, R3, R4, R5, R6, R7 | R6, R7, R1, R2, R3, R4, R5 |
  | TC-FA-LIC-236 | Plan Owner | R7, R1, R2, R3, R4, R5, R6 | R1, R2, R3, R4, R5, R6, R7 |
  | TC-FA-LIC-237 | Quantity | R1, R3, R7, R2, R6, R4, R5 | R5, R4, R6, R2, R7, R3, R1 |
  | TC-FA-LIC-238 | Date | R7, R6, R5, R4, R3, R2, R1 | R1, R2, R3, R4, R5, R6, R7 |
  | TC-FA-LIC-238 | End Date | R7, R6, R1, R2, R3, R4, R5 | R1, R2, R3, R4, R5, R6, R7 |
  | TC-FA-LIC-238 | Last Updated | R7, R6, R5, R4, R3, R2, R1 | R1, R2, R3, R4, R5, R6, R7 |

- State yang diubah: Sort kolom tiap anggota; klik ketiga menetralkannya kembali sehingga tidak perlu pemulihan lain.

## Test Steps

1. Klik sub-tab `Allocation History`

### TC-FA-LIC-236, TC-FA-LIC-237, dan TC-FA-LIC-238: Siklus sort Ascending, Descending, netral

Untuk setiap baris tabel "Anggota sort per kelas kolom" (langkah 2 sampai 7):

2. Klik header kolom baris tabel sekali (Ascending)
3. Verifikasi indikator `↑` dan urutan baris sesuai kolom `Klik 1 (Ascending)` baris tabel
4. Klik header kolom baris tabel sekali lagi (Descending)
5. Verifikasi indikator `↓` dan urutan baris sesuai kolom `Klik 2 (Descending)` baris tabel
6. Klik header kolom baris tabel sekali lagi (netral)
7. Verifikasi urutan baris kembali ke urutan default: LALC-20260801-00004, LALC-20260720-00003, LALC-20260515-00002, LALC-20260312-00002, LALC-20260101-00001, LALC-20250210-00001, LALC-20241205-00001

## Notes

- Sumber: `fixed-asset/license/TestCases/tc-license.md`. Subjudul `###` memetakan langkah ke id TC. Tidak ada TC hanya-BE.
- Spec ini di atas 35 langkah (7 langkah nominal; 55 langkah setelah ekspansi). Alasan: langkah 2 sampai 7 diulang per kolom (sembilan iterasi) dengan parameter di tabel `## Prerequisites`, tanpa langkah bersyarat, dan tiap iterasi memuat satu `Verifikasi` per klausa Expected TC (S-01); semua iterasi satu topik (siklus sort), satu dataset Pre-setup #13 yang hanya dibaca, dan berdiri sendiri.
- TC-FA-LIC-236, 237, dan 238 digabung dalam satu blok ulang karena langkah ujinya identik; tabel Prerequisites memetakan baris ke id TC. Langkah 1 (klik sub-tab sebagai aksi deterministik) adalah langkah penghubung.
- Temuan untuk QA: TC-FA-LIC-236, 237, dan 238 tidak menyebut Post Condition (`-`); tidak ada yang diasersi. Urutan baris bernilai sama (mis. Plan Owner `PT Maju Bersama (Distributor)` pada R1 sampai R6, Status `Active` pada R1 sampai R5) mengikuti Expected TC.

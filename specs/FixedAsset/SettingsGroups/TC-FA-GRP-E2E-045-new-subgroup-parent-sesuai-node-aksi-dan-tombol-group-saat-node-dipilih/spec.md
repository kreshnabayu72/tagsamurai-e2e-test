---
id: TC-FA-GRP-E2E-045-new-subgroup-parent-sesuai-node-aksi-dan-tombol-group-saat-node-dipilih
title: "Create Subgroup: Parent = Node Tempat Aksi Dipicu dan [+] Group Saat Node Dipilih Tetap Membuat Level 1"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-GRP-976
  - TC-FA-GRP-977
coverage:
  web: automated
---

# Create Subgroup: Parent = Node Tempat Aksi Dipicu dan [+] Group Saat Node Dipilih Tetap Membuat Level 1

## Prerequisites

- Mode: FE+BE (backend nyata; hasil Create Subgroup dan Create Group dibaca di sidebar dan tabel).
- Akun aktor: Total Control `totalControlGroups_automated_{namaCompany}@qwertysystem.net` (Pre-setup No 1), kredensial `Spectra.env.FA_TC_PASSWORD` (nama env baru, didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman Fixed Asset > Settings > Groups dibuka hook `beforeEach` suite.
- Hook suite (flag Guided Tooltip `fa-settings-groups` seen, sesi API aktor, klien HTTP, fixture BE): lihat `suite.md` bagian Hook suite; tidak ditulis ulang di sini.
- Data Pre-setup (hanya dibaca): Head Office dan Warehouse A (Warehouse A bukan child Head Office; Head Office punya child Floor 2 sebagai anchor positif).
- Data Dinamis bersuffix `{runId}-045` (nilai diacu lewat `Fixture.fixedAssetSettingsGroups.<kunci>`; berkas fixture belum ada, dibuat di tahap script): TC-FA-GRP-976: `Rack Parent Check {runId}-045`. TC-FA-GRP-977: `Root From Selected {runId}-045`.
- Pemulihan (hook `after`): hapus lewat API semua group dengan suffix `{runId}-045`.
- State global: tidak ada yang diubah.

## Test Steps

### TC-FA-GRP-976: Parent = node tempat aksi dipicu (elipsis sidebar node lain dari node terpilih)

1. Klik Head Office di sidebar
2. Buka elipsis (⋯) node Warehouse A di sidebar, lalu klik Add Subgroup
3. Verifikasi baris konteks Under = Warehouse A (bukan Head Office)
4. Isi Group Name `Rack Parent Check {runId}-045`, lalu klik [Submit]
5. Verifikasi `Rack Parent Check {runId}-045` dibuat sebagai child Warehouse A di sidebar
6. Klik Head Office di sidebar
7. Verifikasi tabel Head Office menampilkan Floor 2
8. Verifikasi `Rack Parent Check {runId}-045` tidak muncul sebagai child Head Office

### TC-FA-GRP-977: [+] Group saat node dipilih tetap membuat group level 1 tanpa parent

9. Klik Head Office di sidebar, lalu klik [+] Group
10. Verifikasi popup New Group tampil tanpa baris konteks Under
11. Isi Group Name `Root From Selected {runId}-045`, lalu klik [Submit]
12. Klik All Groups
13. Ketik Search `Root From Selected {runId}-045`, tekan Enter
14. Verifikasi `Root From Selected {runId}-045` muncul sebagai node level 1 (tanpa parent) di tabel All Groups
15. Verifikasi `Root From Selected {runId}-045` muncul sebagai node level 1 di sidebar
16. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel
17. Klik Head Office di sidebar
18. Verifikasi tabel Head Office menampilkan Floor 2
19. Verifikasi tabel Head Office tidak memuat `Root From Selected {runId}-045`

## Notes

- Mode: FE+BE (backend nyata). Sumber: `fixed-asset/settings-groups/TestCases/tc-settings-groups.md`. Subjudul `###` memetakan langkah ke TC granular.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`; S-03): langkah 6 (Klik Head Office di sidebar); langkah 17 (Klik Head Office di sidebar); langkah 13 (Ketik Search `Root From Selected {runId}-045`, tekan Enter) menemukan baris target karena client punya lebih dari 10 node level 1 dengan page size 10, sehingga baris tidak diandalkan berada di halaman 1; langkah 16 (`(←)` pada kotak Search) mengembalikan tabel penuh sebelum memilih Head Office (R-16).
- Asersi absence pada tabel Head Office didahului `Verifikasi` Floor 2 tampil pada surface yang sama (8b butir 2).
- Temuan untuk QA:
  - TC-FA-GRP-976 Expected b "tidak muncul sebagai child Head Office" tidak menyebut langkah memilih Head Office kembali; spec menambahkannya sebagai langkah penghubung.
  - TC-FA-GRP-977 Langkah Uji tidak menyebut verifikasi sesudah [Submit] bahwa toast sukses tampil; spec mengikuti Expected TC (tanpa toast).


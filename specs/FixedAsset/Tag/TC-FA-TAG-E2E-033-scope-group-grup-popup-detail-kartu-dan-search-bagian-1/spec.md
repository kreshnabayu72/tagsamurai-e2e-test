---
id: TC-FA-TAG-E2E-033-scope-group-grup-popup-detail-kartu-dan-search-bagian-1
title: "Scope Group: Grup, Popup Detail, dan Nilai Kartu per Role (Bagian 1)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-TAG-30
  - TC-FA-TAG-131
  - TC-FA-TAG-132
  - TC-FA-TAG-133
  - TC-FA-TAG-134
  - TC-FA-TAG-135
  - TC-FA-TAG-136
  - TC-FA-TAG-137
coverage:
  web: automated
---

# Scope Group: Grup, Popup Detail, dan Nilai Kartu per Role (Bagian 1)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: tabel "Role yang diuji". Login di hook `before` spec ini sebagai akun pertama pada tabel; halaman Fixed Asset > TAG dibuka hook `beforeEach` suite. Ganti akun memakai langkah eksplisit di Test Steps; hook `after` mengembalikan sesi ke akun default suite.

Role yang diuji:

| Blok | Role (teks `Role:` TC) | Kode | Email | Env password |
|---|---|---|---|---|
| 1 | Manage asset & TAG (Read + Update) (group Update: Plant A) | MU_GPA | `manageAssetTagReadUpdateGroupUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_GPA_PASSWORD` |
| 2 | Read Only | RO | `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_RO_PASSWORD` |
| 3 | Total Control | TC | `totalControl_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TC_PASSWORD` |
| 4 | Manage asset & TAG (Read + Update) (Update: Plant A) | MU_PA | `manageAssetTagReadUpdateUpdatePlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MU_PA_PASSWORD` |
| 5 | Manage asset & TAG (Read) (Read: Plant A) | MR_PA | `manageAssetTagReadReadPlantA_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PA_PASSWORD` |
| 6 | Manage asset & TAG (Read) (Read: Plant A; Plant A > Line 1 > Zone 1 adalah descendant) | MR | `manageAssetTagRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_PASSWORD` |
| 7 | Manage asset & TAG (Read) (Read: HQ) | MR_HQ | `manageAssetTagReadReadHq_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_TAG_MR_HQ_PASSWORD` |

- Password tidak ditulis di spec atau fixture; nama env bersifat usulan dan didaftarkan tim FE di `spectra.config.ts` dan `.env.example`.
- Guided Tooltip: flag `guided_tooltip_seen_fa-tag` disetel true oleh hook suite (lihat `suite.md`).
- Fixture: `fixtures/fixed-asset-tag.json` belum ada (disediakan tim FE); nilai Pre-setup ditulis literal seperti di TC.
- Data: Pre-setup tab Paired (grup / Group / Tipe TAG / Total / Reported / Non-standard / Not Paired Yet): Excavator 20 Ton / Plant A / RFID / 20 / 0 / 0 / 2; Excavator 20 Ton / Plant B / RFID / 20 / 2 / 5 / 0; Laptop Pro 14 / HQ / NFC, QR / 25 / 1 / 0 / 2; Forklift Manual / Plant A / Non TAG / 10 / 0 / 3 / 0.
- Data: Scope group per role: grup Excavator 20 Ton ada di Plant A (20 aset) dan Plant B (20 aset); untuk blok 6 grup Excavator 20 Ton ada di Plant A, Plant A > Line 1, Plant A > Line 1 > Zone 1, dan Plant B.
- Seed dan pemulihan data Pre-setup di atas idempotent lewat fixture backend (disediakan tim FE/BE) di hook `before` dan `after`; data bernama literal sesuai TC.
- State global: tidak ada state global yang diubah.
- Suite serial: `parallel: false` (lihat `suite.md`).

## Test Steps

### Manage asset & TAG (Read + Update) (group Update: Plant A) (TC-FA-TAG-30)

1. Verifikasi nilai kartu `Reported` = 0, `Non-standard` = 3, dan `Not Paired Yet` = 2 (hanya grup Plant A dan descendant)
2. Verifikasi grup Plant B dan HQ tidak terhitung pada nilai kartu

### Read Only (TC-FA-TAG-131)

3. Ganti akun: logout dari akun Manage asset & TAG (Read + Update) (group Update: Plant A) [MU_GPA], login dengan akun Read Only [RO], lalu buka Fixed Asset > TAG tab Paired
4. Verifikasi empat baris grup (Plant A, Plant B, HQ) tampil
5. Verifikasi nilai kartu mencakup seluruh scope client: `Reported` 3, `Non-standard` 8, `Not Paired Yet` 4

### Total Control (TC-FA-TAG-132)

6. Ganti akun: logout dari akun Read Only [RO], login dengan akun Total Control [TC], lalu buka Fixed Asset > TAG tab Paired
7. Verifikasi empat baris grup tampil, termasuk Plant A, Plant B, dan HQ

### Manage asset & TAG (Read + Update) (Update: Plant A) (TC-FA-TAG-133)

8. Ganti akun: logout dari akun Total Control [TC], login dengan akun Manage asset & TAG (Read + Update) (Update: Plant A) [MU_PA], lalu buka Fixed Asset > TAG tab Paired
9. Verifikasi baris Excavator 20 Ton / Plant A dan Forklift Manual / Plant A tampil
10. Verifikasi baris Excavator 20 Ton / Plant B dan Laptop Pro 14 / HQ tidak tampil

### Manage asset & TAG (Read) (Read: Plant A) (TC-FA-TAG-134 dan TC-FA-TAG-136)

11. Ganti akun: logout dari akun Manage asset & TAG (Read + Update) (Update: Plant A) [MU_PA], login dengan akun Manage asset & TAG (Read) (Read: Plant A) [MR_PA], lalu buka Fixed Asset > TAG tab Paired
12. Verifikasi hanya baris grup Plant A dan descendant yang tampil
13. Verifikasi grup Plant B dan HQ tidak tampil
14. Klik Asset Name `Excavator 20 Ton` pada baris Plant A untuk membuka Popup Detail
15. Verifikasi total Assets pada blok info = 20
16. Verifikasi tabel hanya memuat aset Plant A dan descendant; tidak ada aset Plant B
17. Tutup Popup Detail

### Manage asset & TAG (Read) (Read: Plant A; Plant A > Line 1 > Zone 1 adalah descendant) (TC-FA-TAG-135)

18. Ganti akun: logout dari akun Manage asset & TAG (Read) (Read: Plant A) [MR_PA], login dengan akun Manage asset & TAG (Read) [MR], lalu buka Fixed Asset > TAG tab Paired
19. Verifikasi baris grup Plant A, Line 1, dan Zone 1 tampil (cucu ikut)
20. Verifikasi baris grup Plant B tidak tampil

### Manage asset & TAG (Read) (Read: HQ) (TC-FA-TAG-137)

21. Ganti akun: logout dari akun Manage asset & TAG (Read) [MR], login dengan akun Manage asset & TAG (Read) (Read: HQ) [MR_HQ], lalu buka Fixed Asset > TAG tab Paired
22. Verifikasi nilai kartu `Reported` = 1, `Non-standard` = 0, dan `Not Paired Yet` = 2 (hanya grup HQ)

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md`. Tidak ada TC hanya-BE.
- Spec Role Matrix ditulis per blok role karena ganti akun menuntut Step eksplisit (akun pertama login di hook `before`).
- Langkah penghubung (aksi tanpa `Verifikasi`, bukan dari langkah TC): langkah 3, 6, 8, 11, 17, 18, 21.
- Urutan TC-FA-TAG-136 dan TC-FA-TAG-135 disusun ulang (TC-FA-TAG-136 menyusul TC-FA-TAG-134 karena memakai akun yang sama) supaya akun tidak diganti dua kali untuk Role yang sama; Expected tiap TC tetap diasersi.
- Pembagian TC lintas spec: TC-FA-TAG-138 (Search di luar scope) ada di spec `TC-FA-TAG-E2E-034-scope-group-grup-popup-detail-kartu-dan-search-bagian-2`.
- Temuan untuk QA:
  - Lampiran A konvensi belum memuat butir untuk modul ini: data Pre-setup yang dirujuk TC (nama aset, kode Tag, ID aset, Return Group) ditulis literal tanpa suffix `{runId}` karena asersi bergantung pada nama, urutan, dan jumlah; seeding idempotent dan pemulihan lewat fixture backend (lihat `suite.md`).
  - Role Matrix memakai satu akun Pre-setup per Role; TC tidak menyebut kunci akun, sehingga akun dipilih dari baris Pre-setup bernama dasar sama.
  - TC-131 butir a menyebut "Empat baris grup" tetapi hanya tiga nama group (Plant A, Plant B, HQ); spec menghitung empat baris Pre-setup (Excavator 20 Ton / Plant A, Excavator 20 Ton / Plant B, Laptop Pro 14 / HQ, Forklift Manual / Plant A).
  - TC-134 dan TC-136 memakai Role `Manage asset & TAG (Read) (Read: Plant A)`; TC-135 memakai Role dengan catatan descendant tiga tingkat yang tidak punya baris Pre-setup sendiri, sehingga spec memakai akun `Manage asset & TAG (Read)` dengan capability group yang diatur fixture backend; Pre-setup memuat akun terdekat `Manage asset & TAG (Read) (Read: Plant A)`.

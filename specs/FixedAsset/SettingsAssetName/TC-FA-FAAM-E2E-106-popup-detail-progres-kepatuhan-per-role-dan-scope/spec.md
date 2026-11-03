---
id: TC-FA-FAAM-E2E-106-popup-detail-progres-kepatuhan-per-role-dan-scope
title: "Role Matrix: Progres Kepatuhan TAG Type Client-Wide pada Group Manager, Read Only, dan Permission Read"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-FAAM-831
  - TC-FA-FAAM-834
coverage:
  web: automated
---

# Role Matrix: Progres Kepatuhan TAG Type Client-Wide pada Group Manager, Read Only, dan Permission Read

## Prerequisites

- Mode: FE+BE (backend nyata).
- Role yang diuji (login akun pertama di hook `before` spec ini; halaman Fixed Asset > Settings > Asset Master > Asset Name dibuka hook `beforeEach` suite; akun berikutnya lewat langkah `Ganti akun` eksplisit; hook `after` mengembalikan sesi ke akun default suite, Total Control `Spectra.env.FA_TC_PASSWORD`):

| Urutan | Role | Akun (Pre-setup) | Password | TC |
|---|---|---|---|---|
| 1 | Group Manager (scope Group `Head Office` beserta descendant `Finance`) | #32g `groupManagerAssetName_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_GM_PASSWORD` | TC-FA-FAAM-831 |
| 2 | Read Only | #2 `readOnly_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_RO_PASSWORD` | TC-FA-FAAM-834 |
| 3 | Permission Read | #3 `permissionRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.FA_PR_PASSWORD` | TC-FA-FAAM-834 |

- Hook suite (`suite.md`): `before`, `beforeEach`, dan `after` dirujuk apa adanya; suite berjalan serial (`parallel: false`). Spec ini tidak memakai seed API per TC.
- Data Pre-setup #38 yang hanya dibaca: `Excavator 20 Ton` (TAG Type `RFID`), 40 aset `Active` dalam scope client, Group `Plant A` 20 aset dan Group `Plant B` 20 aset, keduanya di luar Group scope Group Manager; `[Compliant]` 33, `[N]` 40; fixture `Fixture.faAssetName.excavator`. Tidak ada data yang diubah.
- Kemampuan teknis: tidak ada tambahan di luar `suite.md`.
- State global: tidak ada yang diubah spec ini.

## Test Steps

### TC-FA-FAAM-831: Progres kepatuhan client-wide pada Group Manager

1. Ketik Search `Excavator 20 Ton`, tekan Enter
2. Klik nama `Excavator 20 Ton`
3. Verifikasi baris progres menampilkan `33 / 40 assets match the TAG type`
4. Verifikasi `[N]` 40 mencakup aset di Group `Plant A` dan `Plant B` walau berada di luar Group scope aktor, tidak dipotong per group
5. Verifikasi label tab `Total Assets (40)` memuat jumlah client-wide yang sama
6. Klik icon `[✕]` untuk menutup popup

### TC-FA-FAAM-834: Progres kepatuhan sama bagi Read Only dan Permission Read tanpa aksi

7. Ganti akun: logout, lalu login sebagai Read Only `readOnly_automated_{namaCompany}@qwertysystem.net`
8. Buka Fixed Asset > Settings > Asset Master > Asset Name
9. Ketik Search `Excavator 20 Ton`, tekan Enter
10. Klik nama `Excavator 20 Ton`
11. Verifikasi baris progres `33 / 40 assets match the TAG type` tampil di bawah nilai TAG Type
12. Verifikasi baris progres read-only tanpa aksi atau tautan
13. Klik icon `[✕]` untuk menutup popup
14. Ganti akun: logout, lalu login sebagai Permission Read `permissionRead_automated_{namaCompany}@qwertysystem.net`
15. Buka Fixed Asset > Settings > Asset Master > Asset Name
16. Ketik Search `Excavator 20 Ton`, tekan Enter
17. Klik nama `Excavator 20 Ton`
18. Verifikasi baris progres `33 / 40 assets match the TAG type` tampil di bawah nilai TAG Type
19. Verifikasi baris progres read-only tanpa aksi atau tautan
20. Klik icon `[✕]` untuk menutup popup

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-asset-name/TestCases/tc-settings-asset-name.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Spec ditulis per blok role karena ganti akun menuntut langkah eksplisit (akun pertama login di hook `before`); langkah tiap role identik tetapi akunnya berbeda (bagian 3a, susunan spec Role Matrix).
- Langkah penghubung (aksi tanpa `Verifikasi`): Search untuk menemukan baris target (R-16, langkah 1, 9, 16), membuka halaman Asset Name sesudah login akun baru (langkah 8, 15), dan `[✕]` menutup popup (langkah 6, 13, 20).
- Kesamaan dengan tampilan Total Control (TC-FA-FAAM-830) pada TC-FA-FAAM-831 Expected a dan TC-FA-FAAM-834 Expected a diasersi lewat teks baris progres yang persis sama dengan Expected TC-FA-FAAM-830 (spec 105).
- Temuan untuk QA:
  - TC-FA-FAAM-831 Precondition menyebut Pre-setup #32 (Asset Value HO) bersama Role Group Manager; spec memakai akun Group Manager Pre-setup #32g (`groupManagerAssetName_automated_{namaCompany}@qwertysystem.net`) yang cocok dengan Role pada TC.
  - Indeks TC untuk TC-FA-FAAM-834 memuat akun #2 saja; baris TC mentah menyebut Read Only dan Permission Read (Pre-setup #2, #3) dan Langkah Uji memakai kedua role, sehingga spec memakai kedua akun.
  - TC-FA-FAAM-834 Expected b ("tanpa aksi atau tautan") tidak menyebut cara teramati selain tidak adanya ikon, tautan, atau tombol pada baris progres.

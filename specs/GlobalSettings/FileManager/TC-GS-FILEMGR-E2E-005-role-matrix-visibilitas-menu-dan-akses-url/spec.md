---
id: TC-GS-FILEMGR-E2E-005-role-matrix-visibilitas-menu-dan-akses-url
title: "Role Matrix: Visibilitas Menu File Manager dan Akses URL Langsung per Role"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-GS-FILEMGR-40
  - TC-GS-FILEMGR-41
  - TC-GS-FILEMGR-42
coverage:
  web: automated
---

# Role Matrix: Visibilitas Menu File Manager dan Akses URL Langsung per Role

## Prerequisites

- Mode: FE+BE.
- Login akun aktor pertama (Lina Marlina) dilakukan di hook `before`; ganti akun ke role berikutnya ditulis sebagai langkah (langkah 8 dan 10). Hook `after` mengembalikan sesi ke akun default suite (Total Control Sinta Maharani, `GS_TC_PASSWORD`). Password tidak ditulis di spec atau fixture; semua nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.

Role yang diuji (Tabel Data Uji Pre-setup A1; domain `{namaCompany}`):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-GS-FILEMGR-40, TC-GS-FILEMGR-42 | Tanpa akses File Manager | Lina Marlina | `noAccessGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_NOACCESS_PASSWORD` |
| TC-GS-FILEMGR-41 | Total Control | Sinta Maharani | `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| TC-GS-FILEMGR-41 | Read Only | Rina Pratiwi | `readOnlyGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_RO_PASSWORD` |
| TC-GS-FILEMGR-41 | Manage files: Read | Doni Saputra | `manageFilesRead_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_READ_PASSWORD` |
| TC-GS-FILEMGR-41 | Manage files: Delete | Agus Wibowo | `manageFilesDelete_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_FILES_DELETE_PASSWORD` |

- Langkah 10 sampai 13 identik untuk keempat role TC-41 (hanya akun login yang berbeda), ditulis sebagai perulangan "Untuk setiap role" (4 langkah x 4 role = 16 langkah setelah ekspansi).
- Data: spec tidak membuat, mengubah, atau menghapus data; hanya visibilitas menu dan hasil akses URL yang diperiksa. URL halaman Global Settings > File Manager dirujuk dari fixture `Fixture.fileManager.url` (fixture dibuat tahap script).
- Guided Tooltip: flag `guided_tooltip_seen_gs-file-manager` disetel true untuk kelima akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Capability tiap akun adalah data Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-FILEMGR-40: Menu File Manager tidak tampil di sidebar untuk akun tanpa akses File Manager

1. Buka sidebar Global Settings sebagai Lina Marlina
2. Verifikasi sedikitnya satu item menu Global Settings lain tampil di sidebar
3. Verifikasi item menu File Manager tidak ada di sidebar (Hidden) sehingga tidak ada surface File Manager yang dapat dibuka dari navigasi

### TC-GS-FILEMGR-42: Akses langsung ke URL File Manager oleh akun tanpa akses

4. Ketik atau paste URL halaman Global Settings > File Manager langsung di address bar, lalu tekan Enter
5. Verifikasi toast error `You don't have permission to do this.`
6. Verifikasi tidak ada redirect ke halaman unauthorized terpisah
7. Verifikasi tidak ada baris data File Manager yang tampil

### TC-GS-FILEMGR-41: Menu File Manager tampil di sidebar untuk Total Control, Read Only, Manage files: Read, dan Manage files: Delete

8. Logout dari akun Lina Marlina
9. Untuk setiap role pada tabel TC-GS-FILEMGR-41 (Total Control, Read Only, Manage files: Read, Manage files: Delete), lakukan langkah 10 sampai 13
10. Login sebagai role
11. Buka sidebar Global Settings
12. Verifikasi item menu File Manager tampil (Show)
13. Logout

## Notes

- Mode: FE+BE. Sumber: `global-settings/file-manager/TestCases/tc-file-manager.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Penyimpangan urutan: TC-42 ditaruh sebelum TC-41 karena TC-42 memakai akun Lina Marlina yang sama dengan TC-40 (satu login hook `before`); TC-41 butuh ganti akun ke empat role dan diletakkan terakhir. Urutan sumber TC-40, TC-41, TC-42.
- Langkah penghubung (bukan dari TC sumber, tanpa awalan `Verifikasi`): langkah 8 dan 13 (logout), langkah 9 (penanda perulangan), langkah 10 (login per role; ini Step ganti akun eksplisit, S-07).
- Langkah 2 adalah anchor positif untuk asersi absence menu pada langkah 3 (8b butir 2): item menu lain pada sidebar yang sama sudah tampil. TC-40 tidak menyebut item menu lain yang tampil; spec memakai sedikitnya satu item menu Global Settings yang dapat diakses akun itu.
- Langkah 7 (tidak ada baris data) didahului anchor positif toast pada langkah 5.
- Role Matrix mengikuti bagian 3a konvensi: matriks visibilitas boleh memuat polaritas tampil dan Hidden dalam satu spec. TC-40 dan TC-42 satu akun (Lina Marlina), TC-41 satu perulangan empat role.
- Temuan untuk QA:
  - TC-40 dan TC-42 mensyaratkan "halaman Global Settings mana pun" tanpa menyebut halaman awal; spec memulai dari halaman setelah login akun Lina Marlina.
  - TC-42 menyebut "URL halaman File Manager" tanpa menuliskan URL; spec merujuk fixture `Fixture.fileManager.url` (S-13).
  - TC-42 Expected b ("tidak ada redirect ke halaman unauthorized terpisah") tidak merinci halaman yang tampil setelah toast; spec hanya mengasersi tidak ada redirect ke halaman unauthorized terpisah.

---
id: TC-AC-DC-E2E-022-role-matrix-node-hardcoded
title: "Role Matrix: Aksi pada Node Hardcoded Hardware, TAG, dan Node Perantara untuk Total Control"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-57
  - TC-AC-DC-58
coverage:
  web: automated
---
# Role Matrix: Aksi pada Node Hardcoded Hardware, TAG, dan Node Perantara untuk Total Control

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control (Pre-setup #1); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control (`Budi Santoso`) | #1 `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Tabel "Node hardcoded perantara" (Pre-setup #14) untuk langkah berulang TC-AC-DC-58:

| Node hardcoded perantara | Induk |
|---|---|
| `BLE Gateway` | `Hardware` |
| `Handheld Reader` | `Hardware` |
| `Smart Fixed Reader` | `Hardware` |
| `BLE` | `TAG` |
| `GPS` | `TAG` |
| `NFC` | `TAG` |
| `RFID` | `TAG` |

- Data Pre-setup: #14 (Pohon Uji Kategori, hanya dibaca; semua node hanya di-hover). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Spec ini tidak membuat data; tidak ada seeding dan cleanup data.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-57: Hardware dan TAG tidak memiliki aksi apa pun untuk Total Control

1. Expand `Hardware`
2. Expand `TAG`
3. Expand `Handheld Reader`
4. Hover node `Hardware`
5. Verifikasi tidak ada aksi `+ Subcategory`, Edit, atau Delete pada `Hardware`
6. Hover node `TAG`
7. Verifikasi tidak ada aksi `+ Subcategory`, Edit, atau Delete pada `TAG`
8. Hover node `Rugged Scanner` sebagai pembanding
9. Verifikasi pembanding: hover `Rugged Scanner` menampilkan `+ Subcategory`, Edit, dan Delete

### TC-AC-DC-58: Node hardcoded perantara hanya menyediakan + Subcategory untuk Total Control

10. Untuk setiap node pada tabel "Node hardcoded perantara" di Prerequisites (langkah 10 sampai 12): hover node tersebut
11. Verifikasi node tersebut hanya menampilkan aksi `+ Subcategory`
12. Verifikasi Edit dan Delete Hidden pada node tersebut

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Spec Role Matrix visibilitas (kedua polaritas: aksi tampil pada pembanding, Hidden pada node hardcoded) satu role.
- Langkah 10 sampai 12 diulang untuk 7 node pada tabel Prerequisites (ambang 35 langkah dihitung dengan ekspansi: 9 langkah nominal sebelum perulangan ditambah 3 x 7 = 21, total 30).
- Langkah penghubung: langkah 1, 2, 3 (expand tree agar semua node yang di-hover terlihat; `Handheld Reader` di-expand agar pembanding `Rugged Scanner` terlihat).
- Temuan untuk QA:
  - Semua node pada spec ini hanya di-hover; tidak ada aksi tulis pada node Pre-setup.
  - Post Condition TC-AC-DC-57 dan 58 ('-') tidak punya langkah observasi dan tidak diasersi.

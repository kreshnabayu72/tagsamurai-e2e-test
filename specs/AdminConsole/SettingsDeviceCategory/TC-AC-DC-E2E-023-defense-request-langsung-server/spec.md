---
id: TC-AC-DC-E2E-023-defense-request-langsung-server
title: "Defense-in-Depth: Request Langsung terhadap Node Hardcoded Ditolak Server"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-DC-241
  - TC-AC-DC-242
  - TC-AC-DC-243
coverage:
  web: automated
---
# Defense-in-Depth: Request Langsung terhadap Node Hardcoded Ditolak Server

## Prerequisites

- Mode: FE+BE.
- Aktor: Total Control (Pre-setup #1); Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Settings > Device > Device Name).

| Role yang diuji | Akun (Pre-setup) | Password |
|---|---|---|
| Total Control (`Budi Santoso`) | #1 `totalControlDevCat_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_TC_PASSWORD` |

- Kemampuan teknis: sesi API aktor (login API password untuk akun yang sama dengan sesi UI, tidak dihitung sebagai sesi web) dan klien HTTP; disediakan tim BE/FE dan dinyatakan di `suite.md`.
- Data Pre-setup: #14 (Pohon Uji Kategori). Node `Hardware`, `TAG`, dan `Handheld Reader` adalah objek uji (node hardcoded) dan menjadi target request yang diharapkan ditolak server; node itu tidak boleh berubah. Nama yang dikirim di request diberi sufiks `{runId}-023` (`Bypass Root {runId}-023`, `Bypass Root TAG {runId}-023`, `Bypass Edit {runId}-023`, `Bypass Edit Root {runId}-023`). Nilai data mengacu ke fixture `settingsDeviceCategory` (belum ada; disediakan tim FE). Nama node Pre-setup #14 ditulis sebagaimana di TC.
- Kemampuan membaca jumlah entri Changelog Category (disediakan tim FE/BE); jumlah dicatat sebagai baseline di hook `before` sesudah seeding, dan asersi memakai perbandingan terhadap baseline itu.
- Spec ini tidak membuat node; hook `before` hanya mencatat baseline jumlah entri Changelog Category. Hook `after` menghapus node bernama sufiks `{runId}-023` bila ada (cadangan bila server menerima request yang seharusnya ditolak) dan tidak berasumsi baseline tercatat.
- Env var `AC_TC_PASSWORD` sudah terdaftar di `executionConfig.environmentVariables` dan `.env.example`.
- Suite berjalan serial (`parallel: false`): pohon Category, Changelog, dan log audit adalah state bersama.

## Test Steps

### TC-AC-DC-241: Request langsung membuat Category di bawah Hardware atau TAG ditolak

1. Kirim request create Category dengan parent `Hardware` dan nama "Bypass Root {runId}-023" memakai token Total Control
2. Kirim request create Category dengan parent `TAG` dan nama "Bypass Root TAG {runId}-023" memakai token Total Control
3. Verifikasi kedua request ditolak server
4. Muat ulang halaman Device Name
5. Expand `Hardware`
6. Expand `TAG`
7. Verifikasi anak `Hardware` (`BLE Gateway`, `Handheld Reader`, `Smart Fixed Reader`) dan anak `TAG` (`BLE`, `GPS`, `NFC`, `RFID`) tampil
8. Verifikasi tree tidak menampilkan "Bypass Root {runId}-023" maupun "Bypass Root TAG {runId}-023"
9. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-242: Request langsung mengubah nama node hardcoded ditolak

10. Kirim request update nama node `Handheld Reader` menjadi "Bypass Edit {runId}-023" memakai token Total Control
11. Kirim request update nama node `Hardware` menjadi "Bypass Edit Root {runId}-023" memakai token Total Control
12. Verifikasi kedua request ditolak server dengan HTTP 403
13. Muat ulang halaman Device Name
14. Expand `Hardware`
15. Verifikasi nama `Handheld Reader` dan `Hardware` tidak berubah
16. Verifikasi jumlah entri Changelog Category sama dengan baseline

### TC-AC-DC-243: Request langsung menghapus node hardcoded ditolak

17. Kirim request delete node `Handheld Reader` memakai token Total Control
18. Kirim request delete node `TAG` memakai token Total Control
19. Verifikasi kedua request ditolak server dengan HTTP 403
20. Muat ulang halaman Device Name
21. Expand `Hardware`
22. Expand `Handheld Reader`
23. Expand `TAG`
24. Verifikasi `Handheld Reader` beserta anak langsungnya (`Barcode Handheld`, `bluetooth Reader`, `Dipakai Leaf`, `Filter Induk`, `Hapus Daun`, `Hapus Keluarga`, `Industrial Scanner`, node bernama 120 karakter, `Referensi Banyak`, `Rugged Scanner`) dan `TAG` beserta anak langsungnya (`BLE`, `GPS`, `NFC`, `RFID`) tetap ada
25. Verifikasi jumlah entri Changelog Category sama dengan baseline

## Notes

- Mode: FE+BE. K-1: Expected TC-AC-DC-241, 242, dan 243 berupa respons API dan state data; TC tetap di spec FE+BE walau tumpang tindih dengan `tc-settings-device-category-backend.md`. Sumber: `admin-console/settings-device-category/TestCases/tc-settings-device-category.md`.
- Subjudul `###` memetakan langkah ke id TC granular.
- Request langsung dikirim lewat klien HTTP, tidak melewati browser (8b butir 1); asersi hanya status respons dan state data. Muat ulang halaman Device Name dan pemeriksaan tree adalah observasi state data seperti langkah TC.
- Langkah penghubung: langkah 5 sampai 23 (expand tree sesudah muat ulang agar node yang diperiksa terlihat; pohon dianggap kembali tertutup sesudah muat ulang, seperti TC lain yang selalu memulai dengan expand).
- Tiga TC di spec ini berupa blok independen satu kelas harness (kelas a) dengan baseline Changelog bersama; kegagalan satu blok tidak mengurangi makna blok lain.
- Asersi "Changelog tidak bertambah" ditulis sebagai asersi jumlah dengan baseline (S-12), bukan asersi absence kelas g; TC-AC-DC-241, 242, dan 243 tidak punya spec absence yang memuat request ini.
- Anchor absence: langkah 7 (anak `Hardware` dan `TAG` tampil) mendahului asersi "tree tidak menampilkan" Bypass Root pada langkah 8 (8b butir 2).
- Temuan untuk QA:
  - Request pada TC-AC-DC-242 dan 243 menarget node hardcoded Pre-setup `Handheld Reader`, `Hardware`, dan `TAG` (objek uji); bila server keliru menerima request, pohon Pre-setup rusak dan butuh pemulihan fixture backend (S-06). Node itu tidak dapat diganti node milik spec karena yang diuji justru kebalnya node hardcoded.
  - TC-AC-DC-241 Expected a ("ditolak server") tidak menyebut status respons; asersi mengikuti kalimat TC tanpa kode status.
  - Mekanisme klien HTTP dan endpoint tidak disebut TC; tidak dikarang (S-13), disediakan tim BE/FE.
  - Post Condition TC-AC-DC-241, 242, dan 243 ('-') tidak punya langkah observasi dan tidak diasersi.

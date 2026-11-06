---
id: TC-FA-TAG-E2E-346-state-tenant-plan-free-tipe-tag-terkunci-pada-replace-dan-pair-bagian-2
title: "State Tenant: Free Plan pada Tag Non-standard, Bulk Batch Replace, Tampilan Tab Paired, Menu TAG, dan Upgrade Plan (Bagian 2)"
priority: Medium
caseType: Edge
status: draft
sourceTc:
  - TC-FA-TAG-376
  - TC-FA-TAG-383
  - TC-FA-TAG-1154
  - TC-FA-TAG-1314
  - TC-FA-TAG-1315
coverage:
  web: automated
---

# State Tenant: Free Plan pada Tag Non-standard, Bulk Batch Replace, Tampilan Tab Paired, Menu TAG, dan Upgrade Plan (Bagian 2)

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (`totalControl_automated_{namaCompany}@qwertysystem.net`, `Spectra.env.FA_TC_PASSWORD`). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Nama env didaftarkan di `executionConfig.environmentVariables` dan `.env.example`.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_fa-tag` true untuk akun aktor yang dipakai dan hook suite `after` memulihkannya (lihat `suite.md`).
- Suite serial: `parallel: false` (lihat `suite.md`), karena spec mengubah plan Client.
- Kemampuan teknis (disediakan tim FE/BE): (1) perubahan plan Client (Free plan: hanya Tag QR yang dikelola) lewat fixture backend, dan upgrade plan ke plan yang mengizinkan Tag RFID oleh pelaku kedua (Admin) lewat sesi API (login API password, tidak dihitung sebagai sesi web; lihat `suite.md`); akun Admin disediakan tim FE; hook `before` menyetel Client ke Free plan dan hook `after` memulihkan plan awal; (2) seed dan pemulihan idempotent lewat fixture backend untuk aset dan stok Tag per tipe di registri Global; (3) simulator reader RFID/NFC USB tersambung dan aktif sebagai precondition TC-FA-TAG-376 dan 1154 (tidak diasersi); (4) penanganan dialog `beforeunload` (konfirmasi otomatis saat halaman dimuat ulang dengan dialog atau Popup Detail terbuka; bila dialog belum terisi, konfirmasi itu tidak muncul dan halaman langsung dimuat ulang), dipakai untuk menutup dialog lewat muat ulang halaman (F5) pada langkah 8, 13, dan 27 (S-08, A-16). Tidak ada endpoint yang dikarang di spec ini.
- Data Pre-setup (kunci fixture `Fixture.fixedAssetTag.<kunci>` belum ada; ditandai untuk dibuat tim FE):

| Data | Nilai | Kunci |
|---|---|---|
| Aset Non-standard | 'Excavator 20 Ton - 70' (AST-0070, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag QR `QR-00305` Paired (Non-standard) | `aset70` |
| Aset Paired | 'Excavator 20 Ton - 220' (AST-0220, Group Plant A, TAG Type Asset Name RFID) dengan satu Tag RFID `RF-00330` Paired | `aset220` |
| Stok Global Available | Tag RFID `RF-00412`, `RF-00415`, `RF-00420`, Tag NFC `NF-00500`, Tag QR `QR-00701` | `stokAvailable` |
| Grup tab Paired | 'Excavator 20 Ton' / Plant A / RFID / Total 20 / Reported 0 / Non-standard 0 / Not Paired Yet 2; 'Excavator 20 Ton' / Plant B / RFID / 20 / 2 / 5 / 0; 'Laptop Pro 14' / HQ / NFC, QR / 25 / 1 / 0 / 2; 'Forklift Manual' / Plant A / Non TAG / 10 / 0 / 3 / 0 | `grupPaired` |

- State yang diubah dan pemulihannya: Client berada di Free plan dari awal spec; langkah 26 meng-upgrade plan ke plan yang mengizinkan Tag RFID. Hook `after` memulihkan plan awal Client lewat fixture backend walau spec gagal di tengah. Tidak ada data aset yang berubah (semua aksi hanya membaca atau dialog ditutup).
- Nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}`: pengecualian S-06/S-12 butir A-15. Seeding idempotent (dilewati bila sudah ada) dan pemulihan lewat fixture BE; suite serial (`parallel: false`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi tulis TAG (dialog Replace TAG pada langkah 5 hanya dibuka lalu ditutup lewat muat ulang halaman). Upgrade plan Client lewat sesi API (langkah 26) dipulihkan oleh hook `after`; PRD tag.md dan TC tidak menyatakan efek tak terpulihkan untuk upgrade itu.

## Test Steps

### TC-FA-TAG-376: Row action Replace TAG Enabled untuk Tag Non-standard

1. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
2. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 70'
3. Klik row action `Replace TAG`
4. Verifikasi row action `Replace TAG` Enabled
5. Verifikasi Dialog Replace TAG terbuka
6. Verifikasi bagian `Replacement TAG` tidak memuat slot RFID
7. Verifikasi Alert info berisi "This TAG type is not available on your plan."
8. Muat ulang halaman (F5)

### TC-FA-TAG-383: Bulk Batch Replace TAG Hidden

9. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
10. Centang baris 'Excavator 20 Ton - 220'
11. Verifikasi Bulk Action Bar tampil
12. Verifikasi Bulk Action Bar tidak memuat `Batch Replace TAG` (Hidden)
13. Muat ulang halaman (F5)

### TC-FA-TAG-1314: Tag tipe terkunci tetap tampil di tab Paired

14. Buka tab Paired
15. Klik Asset Name 'Excavator 20 Ton' pada baris Plant B
16. Verifikasi Tag RFID tetap tampil pada baris grup (tidak disembunyikan)
17. Verifikasi Tag RFID tetap tampil pada Popup Detail (tidak disembunyikan)
18. Tutup Popup Detail dengan ikon close

### TC-FA-TAG-1315: Menu TAG tidak plan-gated

19. Verifikasi menu `TAG` tampil pada sidebar Fixed Asset
20. Klik menu `TAG`
21. Verifikasi halaman Fixed Asset > TAG dapat dibuka

### TC-FA-TAG-1154: Plan diupgrade, row action Replace TAG tidak lagi Disabled

22. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
23. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
24. Verifikasi row action `Replace TAG` Disabled
25. Verifikasi tooltip "This TAG type is not available on your plan."
26. Pelaku kedua (Admin) meng-upgrade plan Client ke plan yang mengizinkan Tag RFID lewat sesi API hingga tersimpan
27. Muat ulang halaman (F5)
28. Klik Asset Name 'Excavator 20 Ton' pada baris grup Plant A untuk membuka Popup Detail
29. Arahkan kursor ke row action `Replace TAG` pada baris 'Excavator 20 Ton - 220'
30. Verifikasi row action `Replace TAG` Enabled

## Notes

- Sumber: `fixed-asset/tag/TestCases/tc-tag.md` (TC-FA-TAG-376, 383, 1154, 1314, 1315). Tidak ada TC hanya-BE.
- Urutan TC di spec: TC-FA-TAG-376, 383, 1314, 1315, lalu 1154, karena TC-FA-TAG-1154 meng-upgrade plan dan TC lain membutuhkan Free plan.
- Pembagian TC lintas spec: kasus Free plan pada scan Replace dan row action (TC-FA-TAG-245, 263, 375) ada di spec 345; kasus plan yang mengunci Tag NFC (TC-FA-TAG-307, 308, 365) ada di spec 347 dan (TC-FA-TAG-425, 1476) di spec 384.
- Langkah penghubung (aksi tanpa awalan `Verifikasi`, bukan dari langkah TC): langkah 8, 13, dan 27 (muat ulang halaman untuk menutup dialog atau Popup Detail dan membersihkan seleksi; dialog `beforeunload` ditangani sesuai Prerequisites), 14 (membuka tab Paired), 18 (menutup Popup Detail), 28 (membuka kembali Popup Detail sesudah muat ulang; TC-FA-TAG-1154 hanya menyebut hover pada baris yang sama).
- Langkah 12 (Batch Replace TAG Hidden) didahului `Verifikasi` Bulk Action Bar tampil di langkah 11 sebagai anchor positif; langkah 4 sampai 7 mengikuti urutan Expected TC-FA-TAG-376.
- A-15: nilai literal Pre-setup (Asset Name, ID aset AST-*, kode Tag RF-*/NF-*/QR-*) dipakai tanpa suffix `{runId}` karena asersi bergantung pada nama dan kode persis; ini pengecualian S-06/S-12 dengan seeding idempotent (dilewati bila sudah ada), pemulihan lewat fixture BE, dan suite serial (`parallel: false`, lihat `suite.md`). Efek yang tidak terpulihkan: tidak ada yang dinyatakan PRD tag.md atau TC; spec ini tidak menjalankan aksi tulis TAG (dialog Replace TAG pada langkah 5 hanya dibuka lalu ditutup lewat muat ulang halaman). Upgrade plan Client lewat sesi API (langkah 26) dipulihkan oleh hook `after`; PRD tag.md dan TC tidak menyatakan efek tak terpulihkan untuk upgrade itu.
- Temuan untuk QA:
  - TC-FA-TAG-383 tidak menyebut teks penghitung seleksi pada Bulk Action Bar; langkah 11 hanya mengasersi Bulk Action Bar tampil sebagai anchor positif untuk asersi absence `Batch Replace TAG` pada langkah 12 (bagian 8b butir 2; asersi tambahan, S-03).
  - Post Condition TC-FA-TAG-1314 dan 1315 ("Tidak ada perubahan data bisnis") tanpa langkah observasi di TC tidak diasersi.
  - TC-FA-TAG-1314 menyebut "Aset Free plan ber-Tag RFID" tanpa kode aset; spec memakai baris grup 'Excavator 20 Ton' / Plant B dari data Pre-setup tab Paired.
  - TC-FA-TAG-1315 hanya menyebut "Amati sidebar Fixed Asset"; langkah 20 dan 21 menambah klik menu `TAG` dan `Verifikasi` halaman terbuka sesuai Expected ("halaman dapat dibuka").
  - Fixture `fixtures/fixed-asset-tag.json` belum ada; kunci pada tabel data ditandai untuk dibuat tim FE.

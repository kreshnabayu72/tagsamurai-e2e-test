---
id: TC-AC-RP-E2E-112-state-tenant-entitas-suspended
title: "State Tenant: Entitas Suspended (Kontrol Tulis Enabled, Server Menolak Aksi Tulis, dan Data Tetap Terbaca)"
priority: Critical
caseType: Negative
status: draft
sourceTc:
  - TC-AC-RP-391
  - TC-AC-RP-392
  - TC-AC-RP-393
coverage:
  web: automated
---

# State Tenant: Entitas Suspended (Kontrol Tulis Enabled, Server Menolak Aksi Tulis, dan Data Tetap Terbaca)

## Prerequisites

- Mode: FE+BE (backend nyata; seeding via API).
- Akun aktor: Total Control Distributor Suspended `totalControlSuspRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Yoga Pratama`, Pre-setup #20), password dari `Spectra.env.AC_RP_SUSP_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite (Siti Nurhaliza). Tidak ada ganti akun di tengah spec.
- Data Pre-setup (Tabel Data Uji Pre-setup TC): #20 (`Distributor Suspended` berstatus Suspended; Total Control `Yoga Pratama`), #25 (klien HTTP untuk request langsung ke endpoint modul), dan #26. Pre-setup #11 sampai #18 tidak dipakai karena entitas ini Distributor.
- Data Dinamis: spec ini tidak membuat entitas baru; kontrol diamati dan request ditolak tanpa mengubah data, sehingga suffix `+{runId}-112` dan pemulihan baseline tidak dibutuhkan.
- Tabel "Tab yang dibuka" (TC-AC-RP-393):

| No | Tab |
|---|---|
| 1 | `Total Control` |
| 2 | `Read Only` |
| 3 | `Group Manager` |
| 4 | `System` |

- Kemampuan teknis: klien HTTP untuk request langsung (Pre-setup #25) memakai sesi API aktor `Yoga Pratama` (dinyatakan di `suite.md`); payload request Assign Total Control, Edit CRUD, Assign GM, dan Toggle mengikuti kontrak endpoint modul yang disediakan tim BE (tidak ditulis di TC).
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Env var yang dipakai spec ini (`AC_RP_SUSP_TC_PASSWORD`) baru dan belum terdaftar di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example`; pendaftaran dilakukan di tahap script atau oleh pemilik repo e2e.
- Suite berjalan serial (`parallel: false`) karena status entitas (Suspended) adalah state bersama.
- Fixture `fixtures/settings-role-permission.json` belum ada (ditandai); nama user, role, dan group di langkah mengikuti Tabel Data Uji Pre-setup TC.

## Test Steps

### TC-AC-RP-391: Kontrol tulis tetap enabled saat entitas suspended

1. Verifikasi `[+ Assign]` dan `Remove` pada baris user lain tampil Enabled (tidak Disabled, tidak Hidden)
2. Hover `[+ Assign]`
3. Verifikasi tidak ada tooltip khusus entitas suspended pada `[+ Assign]`
4. Hover `Remove` pada baris user lain
5. Verifikasi tidak ada tooltip khusus entitas suspended pada `Remove`
6. Klik tab `System`
7. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
8. Klik node `Default Group`
9. Verifikasi checkbox CRUD dan toggle tampil Enabled (tidak Disabled, tidak Hidden)
10. Verifikasi kontrol Approvers (`[+ Assign]`, `Remove`, `Bulk Action`) tampil Enabled (tidak Disabled, tidak Hidden)

### TC-AC-RP-392: Server menolak aksi tulis saat entitas suspended

11. Kirim request Assign Total Control secara langsung ke endpoint modul
12. Verifikasi respons request Assign Total Control berstatus 403 Forbidden
13. Kirim request Edit CRUD secara langsung ke endpoint modul
14. Verifikasi respons request Edit CRUD berstatus 403 Forbidden
15. Kirim request Assign GM secara langsung ke endpoint modul
16. Verifikasi respons request Assign GM berstatus 403 Forbidden
17. Kirim request Toggle secara langsung ke endpoint modul
18. Verifikasi respons request Toggle berstatus 403 Forbidden

### TC-AC-RP-393: Entitas suspended tetap dapat melihat data

19. Buka halaman `Settings > Role & Permission` (Tab Total Control aktif)
20. Untuk setiap baris tabel "Tab yang dibuka" pada Prerequisites, lakukan langkah 21 sampai 22
21. Klik tab sesuai baris tabel
22. Verifikasi tab sesuai baris tabel terbuka dan isinya tampil
23. Buka modal Changelog lewat Table Tools
24. Verifikasi modal Changelog terbuka
25. Tutup modal Changelog
26. Verifikasi Download tersedia dan Enabled di Table Tools

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Subjudul `###` memetakan langkah ke id TC granular.
- Langkah berulang (bagian 8b butir 7): langkah 21 dan 22 diulang per baris tabel "Tab yang dibuka" (`Total Control`, `Read Only`, `Group Manager`, `System`; empat iterasi).
- K-1: TC-AC-RP-392 adalah TC defense-in-depth dengan Expected respons API (kelas a); tetap masuk spec FE+BE walau tumpang tindih dengan `tc-settings-role-permission-backend.md` karena tiap TC tepat satu spec; BE mencatatnya pada tingkat endpoint.
- P-5: TC-AC-RP-392 adalah satu TC objek-uji ringan kelas a (tanpa harness eksternal dan tanpa state berat) pada spec kelas h dengan permukaan yang sama (entitas Suspended); jumlahnya satu (batas dua).
- Request langsung (bagian 8b butir 1): TC-AC-RP-392 hanya mengasersi status respons; toast baku "Changes can't be saved while this workspace is suspended or expired." tidak diasersi di spec ini karena perilaku FE atas respons yang sama diasersi pada jalur form (TC-AC-RP-414, spec 135).
- Temuan untuk QA:
  - TC-AC-RP-392 Expected memuat toast baku sebagai hasil request langsung; request langsung tidak melewati browser sehingga toast tidak diasersi (bagian 8b butir 1). Tidak ada TC jalur form untuk entitas Suspended yang mengasersi toast itu; TC-AC-RP-414 mengasersinya untuk entitas Expired.
  - TC-AC-RP-392 tidak menyebut data target request (user, group, role); spec menulis request tanpa target spesifik dan payload mengikuti kontrak endpoint dari tim BE (S-13). Pengecekan state data tidak berubah (8b butir 1) tidak ada di Expected sehingga tidak diasersi.
  - TC-AC-RP-391 Expected "hover tiap kontrol" lebih luas daripada Langkah (hanya hover `[+ Assign]` dan `Remove`); spec mengikuti Langkah dan mengasersi Enabled untuk kontrol lain.
  - TC-AC-RP-393 Expected "Download ... dapat dibuka" tidak punya langkah membuka Download; spec mengasersi Download tersedia dan Enabled tanpa mengunduh.

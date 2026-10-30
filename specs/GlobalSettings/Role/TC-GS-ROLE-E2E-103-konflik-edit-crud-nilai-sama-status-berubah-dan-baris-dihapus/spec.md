---
id: TC-GS-ROLE-E2E-103-konflik-edit-crud-nilai-sama-status-berubah-dan-baris-dihapus
title: "Konflik Antar Admin pada Edit CRUD: Nilai Sama, Status Total Control Berubah, dan Baris Sudah Dihapus"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-ROLE-272
  - TC-GS-ROLE-273
  - TC-GS-ROLE-284
coverage:
  web: automated
---

# Konflik Antar Admin pada Edit CRUD: Nilai Sama, Status Total Control Berubah, dan Baris Sudah Dihapus

## Prerequisites

- Mode: FE+BE. Kelas harness: multi-konteks (dua admin), kelas c. Suite `parallel: false`.
- Akun Sesi A (UI):

| Aktor | TC | Email | Env var password |
|---|---|---|---|
| Ahmad Fauzi (Total Control, akun hook `before`) | TC-272, TC-284 | `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |
| Hendra Wijaya (Manage user and role C/R/U/D) | TC-273 | `manageUserAndRoleCrud_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.GS_ROLE_MANAGE_CRUD_PASSWORD` (env baru) |

- Akun Sesi B (pemicu): Eko Prasetyo (Total Control kedua, Pre-setup #13), email disediakan tim FE, password `Spectra.env.GS_TC2_PASSWORD`. Sesi B memakai sesi API (klien HTTP dengan kredensial Eko Prasetyo; cara memperoleh token disediakan tim FE) karena Sesi B hanya memicu perubahan state dan tidak ada asersi di Sesi B.
- Env baru yang dipakai spec ini: `GS_ROLE_MANAGE_CRUD_PASSWORD` (belum terdaftar di `spectra.config.ts` dan `.env.example`; didaftarkan tim FE). Password tidak ditulis di spec atau fixture.
- Kemampuan teknis: satu konteks browser untuk Sesi A (ganti akun Ahmad Fauzi ke Hendra Wijaya lewat logout dan login); klien HTTP untuk Sesi B; langkah dijalankan berurutan dengan penanda `[Sesi A]` dan `[Sesi B]`.
- Data Dinamis milik spec (dibuat lewat sesi API Eko Prasetyo di hook `before` supaya System Log Ahmad Fauzi tidak memuat entri seeding; kemampuan seeding user dan Assign Role disediakan tim FE; nilai field wajib lain user seed disediakan tim FE). Setara user TC: Doni Pratama (TC-272), Wawan Setiawan (TC-273, TC-284). Semua user Active, Access Global Settings dicentang, tanpa access level:
  - `Target Nilai Sama {runId}-103`: baris Manage TAG dengan Read checked dan Update unchecked (TC-272, dan baris pembanding TC-284).
  - `Target Status Berubah {runId}-103`: baris Manage TAG (TC-273).
  - `Target Dihapus {runId}-103`: baris Manage TAG (TC-284).
- Cleanup di hook `after` (tidak berasumsi seeding berhasil penuh): cabut Total Control `Target Status Berubah {runId}-103` bila ada, hapus baris Manage TAG ketiga user, lalu hapus ketiga user; pulihkan sesi ke akun default suite.
- Flag Guided Tooltip `guided_tooltip_seen_gs-role`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- Layar awal (Global Settings > Role & Permission) dibuka di hook `beforeEach`.
- State global yang diubah: tidak ada selain data milik spec di atas.

## Test Steps

### TC-GS-ROLE-272: Edit CRUD saat admin lain sudah mengubah cell yang sama ke nilai yang sama

1. [Sesi A] Buka Detail "Manage TAG"
2. [Sesi B] Centang Update baris `Target Nilai Sama {runId}-103` lewat sesi API (Edit CRUD Update=true)
3. [Sesi A] Centang Update baris `Target Nilai Sama {runId}-103` tanpa memuat ulang
4. [Sesi A] Verifikasi toast sukses `Success, permissions have been updated.` tampil
5. [Sesi A] Verifikasi tidak ada dialog konflik
6. [Sesi A] Verifikasi Update baris `Target Nilai Sama {runId}-103` tetap tercentang
7. [Sesi A] Klik `Changelog`
8. [Sesi A] Ketik Search `Target Nilai Sama {runId}-103`, tekan Enter
9. [Sesi A] Verifikasi Changelog Detail "Manage TAG" memuat tepat 1 entri Update untuk `Target Nilai Sama {runId}-103` (entri dari Sesi B; Save Sesi A tidak menambah entri)
10. [Sesi A] Tutup modal Changelog
11. [Sesi A] Buka Global Settings > User > Ahmad Fauzi > Tab System Log
12. [Sesi A] Ketik Search `Target Nilai Sama {runId}-103`, tekan Enter
13. [Sesi A] Verifikasi `No results found` tampil (System Log Ahmad Fauzi tidak memuat entri Edit untuk `Target Nilai Sama {runId}-103`)
14. [Sesi A] Buka Global Settings > Activity Log
15. [Sesi A] Ketik Search `Target Nilai Sama {runId}-103`, tekan Enter
16. [Sesi A] Verifikasi Activity Log memuat tepat 1 entri Edit untuk `Target Nilai Sama {runId}-103` dengan Field `Manage TAG — Update` (entri dari Sesi B)

### TC-GS-ROLE-284: Edit CRUD pada baris yang sudah dihapus admin lain

17. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
18. [Sesi B] Remove baris Manage TAG `Target Dihapus {runId}-103` lewat sesi API
19. [Sesi A] Centang Update baris `Target Dihapus {runId}-103` tanpa memuat ulang
20. [Sesi A] Verifikasi toast netral `This permission is no longer available.` tampil
21. [Sesi A] Verifikasi tidak ada toast sukses
22. [Sesi A] Verifikasi tidak ada dialog
23. [Sesi A] Verifikasi baris `Target Nilai Sama {runId}-103` tampil di Detail "Manage TAG" yang di-refresh
24. [Sesi A] Verifikasi baris `Target Dihapus {runId}-103` tidak ada di Detail "Manage TAG"

### TC-GS-ROLE-273: Edit CRUD target yang status Total Control-nya berubah sejak render

25. [Sesi A] Ganti akun: logout, lalu login sebagai Hendra Wijaya
26. [Sesi A] Buka Global Settings > Role & Permission > System > Detail "Manage TAG"
27. [Sesi B] Tetapkan Total Control ke `Target Status Berubah {runId}-103` lewat sesi API
28. [Sesi A] Centang Update baris `Target Status Berubah {runId}-103`
29. [Sesi A] Verifikasi toast error `You don't have permission to edit.` tampil
30. [Sesi A] Verifikasi tidak ada dialog konflik
31. [Sesi A] Verifikasi Update baris `Target Status Berubah {runId}-103` tidak tercentang (perubahan tidak tersimpan)
32. [Sesi A] Verifikasi checkbox Update baris `Target Status Berubah {runId}-103` disabled
33. [Sesi A] Arahkan kursor ke checkbox Update baris `Target Status Berubah {runId}-103`
34. [Sesi A] Verifikasi tooltip `You don't have permission to edit.` tampil

## Notes

- Sumber: `global-settings/role/TestCases/tc-role.md`. Kelas harness: multi-konteks (dua admin), prinsip 13c bagian 3 konvensi; spec konflik antar admin lain ada di `TC-GS-ROLE-E2E-104-konflik-remove-baris-sudah-dihapus-atau-menjadi-total-control`, `TC-GS-ROLE-E2E-105-konflik-remove-access-level-sudah-di-remove-atau-tier-berbeda`, dan `TC-GS-ROLE-E2E-106-konflik-bulk-remove-sebagian-hilang-status-berubah-dan-nol-berhasil`.
- Sesi B memakai sesi API karena hanya memicu perubahan state dan tidak ada asersi di Sesi B (P-2, `[KEPUTUSAN 2026-10-21]`). Objek asersi adalah perilaku Sesi A sesudah perubahan Sesi B.
- Spec berada di sekitar batas 35 langkah (34 langkah) tanpa melewatinya; ketiga blok satu kelas harness dan berdiri sendiri.
- Urutan TC sumber diubah dari 272, 273, 284 menjadi 272, 284, 273 supaya akun Sesi A berganti dari Ahmad Fauzi ke Hendra Wijaya satu kali (langkah 25).
- Langkah penghubung (aksi tanpa `Verifikasi`): membuka Detail dan layar log (langkah 1, 7, 10, 11, 14, 17, 26), Search (langkah 8, 12, 15), dan ganti akun (langkah 25).
- TC-272 Expected d ("tidak menambah entry di Changelog, System Log, maupun Activity Log; hanya entri dari Save sesi B") diasersi sebagai jumlah: Changelog dan Activity Log memuat tepat 1 entri dari Sesi B (data seed unik per run), sedangkan System Log Ahmad Fauzi (pelaku Sesi A) tidak memuat entri Edit untuk user seed; "No results found" pada Search menjadi anchor absence (bagian 8b butir 2). Seeding dilakukan oleh sesi API Eko Prasetyo supaya System Log Ahmad Fauzi tidak memuat entri seeding dengan nama yang sama.
- Hasil TC-273 Expected c ("UI di-refresh: checkbox Update disabled; tooltip") dipecah menjadi langkah 31 sampai 34; langkah 33 (hover) adalah langkah penghubung supaya tooltip dapat diasersi.
- Temuan untuk QA:
  - TC-272 dan TC-284 tidak menyebut akun Sesi A dan Sesi B ("Dua admin"); spec memakai Ahmad Fauzi (Sesi A) dan Eko Prasetyo (Sesi B).
  - TC-272 Expected d tidak menyebut cara mengamati System Log dan Activity Log untuk menyatakan "tidak menambah entry"; spec memakai Search nama user seed.
  - TC-273 memakai Wawan Setiawan dan TC-284 memakai Wawan Setiawan tanpa Given baris Manage TAG; spec memakai user seed milik spec.
  - TC-273 Expected c ("UI di-refresh") tidak menyebut cara refresh; spec mengasersi hasil akhirnya (disabled dan tooltip).

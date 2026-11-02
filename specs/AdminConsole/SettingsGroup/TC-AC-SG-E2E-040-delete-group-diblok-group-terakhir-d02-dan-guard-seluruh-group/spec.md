---
id: TC-AC-SG-E2E-040-delete-group-diblok-group-terakhir-d02-dan-guard-seluruh-group
title: "Delete Group Diblok karena Group Terakhir (D-02) dan Guard Seluruh Group"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-140
  - TC-AC-SG-141
  - TC-AC-SG-142
  - TC-AC-SG-143
coverage:
  web: automated
---

# Delete Group Diblok karena Group Terakhir (D-02) dan Guard Seluruh Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login pertama di hook `before`) dan akun ganti akun:

| Blok TC | Akun | Email | Env var password |
|---|---|---|---|
| TC-140, TC-143 | Total Control Distributor Satu Group (Pre-setup #22) | `totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_SATU_PASSWORD` |
| TC-141 | Total Control Distributor Tiga Group (Pre-setup #24) | `totalControlTigaGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_TIGA_PASSWORD` |
| TC-142 | Total Control Distributor Dua Group (Pre-setup #23) | `totalControlDuaGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_DUA_PASSWORD` |

- Login di hook `before` spec ini sebagai Total Control Distributor Satu Group; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec (Distributor Satu Group).
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite untuk akun yang dipakai suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (komposisi group entitas adalah objek uji, sehingga entitas Pre-setup dipakai langsung, bukan node milik spec, S-06 pengecualian 2026-10-30):
  - #22 `Distributor Satu Group`: hanya `Default Group` (1 group, seed onboarding).
  - #24 `Distributor Tiga Group`: `Head Office` (level 1) dengan anak `Floor 1` dan `Floor 2`, tanpa entitas.
  - #23 `Distributor Dua Group`: tepat 2 group tanpa entitas, `Gudang Utara` dan `Gudang Selatan`.
- Seed tambahan TC-143 (dipakai sebagai precondition TC, tidak diasersi di luar Expected): satu `Client Bintang` (Active) menempel di `Default Group` entitas Satu Group, dibuat dan dilepas lewat Fixture BE.
- Pemulihan baseline: hook `before` dan `after` memulihkan ketiga entitas ke baseline Pre-setup lewat Fixture BE; langkah 12 memulihkan seed tambahan TC-143 dan langkah 26 memulihkan entitas Dua Group (penghubung antar blok, S-09). Hanya TC-142 yang benar-benar menghapus data (`Gudang Utara`); efek pada Last Updated, Modified By, dan audit trail (Changelog, System Log, Activity Log) dari penghapusan dan pemulihan tidak dipulihkan dan tidak diasersi.
- Kemampuan teknis: Fixture BE (seed tambahan dan pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-140: Delete group satu-satunya milik entitas diblok dengan dialog last group (D-02)

1. Klik ikon `⋯` pada baris `Default Group`
2. Verifikasi menu row action "Delete" pada baris `Default Group` enabled
3. Klik "Delete"
4. Verifikasi dialog blok tampil: title "Cannot Delete Group", body bullet `Default Group` dan "Deleting this group would leave you with no groups. Create another group before deleting this one." dengan satu tombol `[OK]`
5. Klik `[OK]`
6. Verifikasi `Default Group` tetap ada

### TC-AC-SG-143: Guard last group dievaluasi lebih dulu dari guard member

7. Lewat Fixture BE, tautkan satu `Client Bintang` (Active) ke `Default Group` entitas Satu Group hingga tersimpan (precondition TC, tidak diasersi)
8. Klik ikon `⋯` pada baris `Default Group`, lalu pilih "Delete"
9. Verifikasi dialog D-02 (last group) tampil: "Cannot Delete Group" dengan body "Deleting this group would leave you with no groups. Create another group before deleting this one."
10. Verifikasi dialog tidak memuat body dialog member D-03 "This group or its subgroups still have members. Remove all members before deleting."
11. Klik `[OK]`
12. Lewat Fixture BE, lepaskan `Client Bintang` dari `Default Group` hingga tersimpan

### TC-AC-SG-141: Delete node yang beserta subtree-nya adalah seluruh group entitas diblok

13. Ganti akun: logout, lalu login sebagai Total Control Distributor Tiga Group (`totalControlTigaGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_TIGA_PASSWORD`)
14. Buka Settings > Group lewat sidebar
15. Verifikasi tabel menampilkan tiga group: `Head Office`, `Floor 1`, `Floor 2`
16. Klik ikon `⋯` pada baris `Head Office`, lalu pilih "Delete"
17. Verifikasi dialog blok D-02 tampil: title "Cannot Delete Group", body bullet `Head Office` dan "Deleting this group would leave you with no groups. Create another group before deleting this one." dengan satu tombol `[OK]` (tanpa jalur lanjut)
18. Klik `[OK]`

### TC-AC-SG-142: Delete salah satu dari dua group tanpa entitas diizinkan

19. Ganti akun: logout, lalu login sebagai Total Control Distributor Dua Group (`totalControlDuaGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_DUA_PASSWORD`)
20. Buka Settings > Group lewat sidebar
21. Klik ikon `⋯` pada baris `Gudang Utara`, lalu pilih "Delete"
22. Verifikasi dialog warning D-04 "Delete Group" tampil (bukan dialog blok)
23. Klik `[Delete]`
24. Verifikasi toast sukses: "Success, group has been deleted."
25. Verifikasi `Gudang Selatan` tersisa sebagai group terakhir
26. Lewat Fixture BE, pulihkan entitas Dua Group ke baseline (`Gudang Utara` dan `Gudang Selatan`) hingga tersimpan

## Notes

- Langkah penghubung (S-03): langkah 5, 11, dan 18 (`[OK]` menutup dialog blok); langkah 12 dan 26 (pemulihan Fixture BE, S-09); langkah 13, 14, 19, dan 20 (ganti akun dan buka halaman, S-07).
- Perubahan urutan TC (S-10): TC-143 ditempatkan sebelum TC-141 dan TC-142 karena memakai akun Satu Group yang sama dengan TC-140; aksi yang benar-benar menghapus data (TC-142) berada di akhir.
- Temuan untuk QA:
  - TC-AC-SG-140 langkah 2 "Perhatikan tombol Delete pada baris `Default Group`" tidak menyebut lokasi tombol; spec memaknainya sebagai item "Delete" pada menu row action `⋯`.
  - TC-AC-SG-141 Expected "walau entitas memiliki 3 group" tidak menyebut cara cek; spec mengasersi tiga baris pada tabel sebelum Delete.

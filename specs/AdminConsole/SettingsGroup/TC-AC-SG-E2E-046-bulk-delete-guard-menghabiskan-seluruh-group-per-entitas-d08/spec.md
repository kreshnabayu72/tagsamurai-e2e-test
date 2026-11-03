---
id: TC-AC-SG-E2E-046-bulk-delete-guard-menghabiskan-seluruh-group-per-entitas-d08
title: "Bulk Delete: Guard Menghabiskan Seluruh Group per Entitas (D-08)"
priority: Critical
caseType: Edge
status: draft
sourceTc:
  - TC-AC-SG-162
  - TC-AC-SG-165
  - TC-AC-SG-166
  - TC-AC-SG-173
coverage:
  web: automated
---

# Bulk Delete: Guard Menghabiskan Seluruh Group per Entitas (D-08)

## Prerequisites

- Mode: FE+BE.
- Akun aktor (login pertama di hook `before`) dan akun ganti akun:

| Blok TC | Akun | Email | Env var password |
|---|---|---|---|
| TC-162 | Total Control Distributor Dua Group (Pre-setup #23) | `totalControlDuaGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_DUA_PASSWORD` |
| TC-173 | Total Control Distributor Satu Group (Pre-setup #22) | `totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_SATU_PASSWORD` |
| TC-165, TC-166 | Total Control Distributor Tiga Group (Pre-setup #24) | `totalControlTigaGroup_automated_{namaCompany}@qwertysystem.net` | `Spectra.env.AC_SG_TIGA_PASSWORD` |

- Login di hook `before` spec ini sebagai Total Control Distributor Dua Group; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec (Distributor Dua Group).
- Flag Guided Tooltip `guided_tooltip_seen_ac-settings-group` disetel `seen` oleh hook suite untuk akun yang dipakai suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (komposisi group entitas adalah objek uji, sehingga entitas Pre-setup dipakai langsung, S-06 pengecualian 2026-10-30):
  - #23 `Distributor Dua Group`: tepat 2 group tanpa entitas, `Gudang Utara` dan `Gudang Selatan` (T=2, E=2, T-E=0).
  - #22 `Distributor Satu Group`: hanya `Default Group`.
  - #24 `Distributor Tiga Group`: `Head Office` (level 1) dengan anak `Floor 1` dan `Floor 2`, tanpa entitas (T=3, E=3).
- Seluruh aksi Bulk Delete di spec ini ditolak guard (dialog blok); tidak ada group yang dihapus atau diubah, Last Updated tidak berubah. Hook `before` dan `after` memastikan baseline ketiga entitas lewat Fixture BE.
- Kemampuan teknis: Fixture BE (pemulihan baseline entitas uji), disediakan tim FE/BE (lihat `suite.md`).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global.

## Test Steps

### TC-AC-SG-162: Bulk Delete yang menghabiskan seluruh group diblok seluruhnya (D-08)

1. Centang kolom Checkbox pada baris `Gudang Utara` dan `Gudang Selatan`
2. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
3. Verifikasi dialog blok tampil: title "Cannot Delete Groups", body bullet `Gudang Utara` dan `Gudang Selatan` serta "These groups are all that's left. At least one group must always exist — deselect at least one of the groups above and try again." dengan `[OK]`
4. Klik `[OK]`
5. Verifikasi tidak ada group terhapus (`Gudang Utara` dan `Gudang Selatan` masih tampil, tidak ada proses parsial)
6. Verifikasi seleksi dipertahankan ("2 Groups selected")
7. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-173: Baris group satu-satunya tetap dapat dicentang dan diblok saat eksekusi

8. Ganti akun: logout, lalu login sebagai Total Control Distributor Satu Group (`totalControlSatuGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_SATU_PASSWORD`)
9. Buka Settings > Group lewat sidebar
10. Verifikasi checkbox baris `Default Group` enabled
11. Centang kolom Checkbox pada baris `Default Group`
12. Verifikasi baris `Default Group` tercentang
13. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
14. Verifikasi dialog blok single D-02 "Cannot Delete Group" tampil saat eksekusi
15. Klik `[OK]`
16. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-165: Bulk memilih hanya parent yang cascade menghabiskan seluruh group diblok

17. Ganti akun: logout, lalu login sebagai Total Control Distributor Tiga Group (`totalControlTigaGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_TIGA_PASSWORD`)
18. Buka Settings > Group lewat sidebar
19. Centang kolom Checkbox pada baris `Head Office`
20. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
21. Verifikasi seleksi 1 baris collapse ke dialog blok single D-02 ("Cannot Delete Group", bullet `Head Office`) karena E=3 (`Head Office` dan dua turunan) dan T-E=0
22. Klik `[OK]`
23. Klik ikon `×` pada Bulk Actions Bar

### TC-AC-SG-166: Memilih parent dan child sekaligus tidak menghitung ganda pada E

24. Centang kolom Checkbox pada baris `Head Office` dan `Floor 1`
25. Klik `Bulk Action` pada Bulk Actions Bar lalu pilih `Delete`
26. Verifikasi dialog blok D-08 tampil dengan bullet `Head Office` dan `Floor 1` (T=3, E=3 tanpa hitung ganda)
27. Klik `[OK]`
28. Verifikasi tidak ada group terhapus (`Head Office`, `Floor 1`, dan `Floor 2` masih tampil)
29. Klik ikon `×` pada Bulk Actions Bar

## Notes

- Langkah penghubung (S-03): langkah 4, 15, 22, dan 27 (`[OK]` menutup dialog blok); langkah 7, 16, 23, dan 29 (membersihkan seleksi, S-09); langkah 8, 9, 17, dan 18 (ganti akun dan buka halaman, S-07).
- Perubahan urutan TC (S-10): TC-173 (Satu Group) ditempatkan sebelum TC-165 dan TC-166 (Tiga Group) agar ganti akun berurutan satu kali per entitas; TC-AC-SG-163 dan TC-AC-SG-164 (Distributor Tiga Campur, menghapus data) berada di spec 111.
- Temuan untuk QA:
  - TC-AC-SG-165 dan TC-AC-SG-166 mensyaratkan "T=3, E=3" tanpa menjelaskan cara E dihitung di UI; spec hanya mengasersi dialog yang tampil.
  - TC-AC-SG-166 Expected "tidak ada group terhapus" tidak memberi cara cek; spec mengasersi ketiga group masih tampil.
  - TC-AC-SG-173 Expected "Checkbox enabled dan dapat dicentang" ditulis sebagai dua `Verifikasi` (enabled sebelum dicentang, tercentang sesudahnya).

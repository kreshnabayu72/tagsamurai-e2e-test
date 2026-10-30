---
id: TC-GS-POS-E2E-046-absence-log-edit-no-op-dan-import
title: "Tidak Ada Pencatatan Log untuk Edit No-Op dan untuk Position Hasil Import"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-GS-POS-246
  - TC-GS-POS-249
  - TC-GS-POS-308
coverage:
  web: automated
---

# Tidak Ada Pencatatan Log untuk Edit No-Op dan untuk Position Hasil Import

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control (Budi Santoso) `superAdminGlobalSettings_automated_{namaCompany}@qwertysystem.net` (Pre-setup 1). Login sekali di hook `before` dengan `Spectra.env.GS_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Layar awal: hook `beforeEach` membuka Global Settings > User > Position (sidebar Global Settings, sub-tab Position). Langkah 1 sampai 3 tidak mengulang langkah buka.
- Data Pre-setup: tidak ada yang dipakai.
- Data Dinamis (suffix per run dan nomor spec):
  - `Legal Counsel {runId}-046`, dibuat lewat UI pada langkah 1 sampai 3 sebagai pemicu entri Create yang menjadi anchor positif di tiga surface log (Changelog, Activity Log, System Log Budi Santoso); tidak diubah nilainya oleh spec ini (Edit hanya No-Op). Baseline entri memakai jumlah entri sebelum aksi, dengan Name bersuffix yang unik per run.
  - `Import Probe Analyst {runId}-046` (Data Dinamis No. 35, TC-GS-POS-249): Position milik spec dengan asal Import Type "Position" (precondition c TC), tanpa entri Changelog; seeding di hook `before` memakai jalur Import Type "Position" (kemampuan teknis disediakan tim FE/BE, tanpa endpoint karangan). Spec ini tidak mengubah atau menghapusnya lewat modul Position sehingga syarat TC-GS-POS-249 (dijalankan sebelum TC-GS-POS-275) terpenuhi. Search dan asersi absence memakai nama lengkap bersuffix `{runId}-046`, bukan substring pendek, supaya Position spec lain tidak muncul di hasil.
- Cleanup (hook `after`, tidak berasumsi pembuatan berhasil): hapus lewat API Position `Legal Counsel {runId}-046` dan `Import Probe Analyst {runId}-046` bila masih ada; kosongkan Search tabel Position.
- Guided Tooltip: hook suite `before` menyetel flag `guided_tooltip_seen_gs-position` true untuk akun Total Control dan hook `after` memulihkannya; lihat `suite.md`.
- Kemampuan teknis: seeding Position hasil Import Type "Position" di hook `before` (disediakan tim FE/BE); pembacaan jumlah entri di Popup Changelog, Activity Log, dan tab System Log di Detail User; Search pada ketiga surface.
- State global: tidak ada yang diubah selain flag Guided Tooltip (dipulihkan seperti di atas).

## Test Steps

### Persiapan anchor: Position dibuat lewat UI

1. Klik `[+ Position]`
2. Isi Position Name dengan `Legal Counsel {runId}-046`
3. Klik `[Submit]`

### TC-GS-POS-246: Edit No-Op tidak menghasilkan entri Changelog dan Activity Log

4. Ketik Search `Legal Counsel {runId}-046` pada tabel Position, tekan Enter
5. Klik ikon Changelog, ketik Search `Legal Counsel {runId}-046`, tekan Enter
6. Verifikasi anchor Changelog: tepat 1 entri dengan Action `Create` untuk `Legal Counsel {runId}-046` (baseline jumlah entri = 1)
7. Tutup Popup Changelog dengan `✕`
8. Buka Global Settings > Activity Log, ketik Search `Legal Counsel {runId}-046`, tekan Enter
9. Verifikasi anchor Activity Log: tepat 1 entri dengan Action `Create`, Object `Position`, Name `Legal Counsel {runId}-046` (baseline jumlah entri = 1)
10. Buka Global Settings > User, klik sub-tab Position, ketik Search `Legal Counsel {runId}-046` pada tabel, tekan Enter
11. Klik `⋯` pada baris `Legal Counsel {runId}-046`, pilih `Edit`
12. Klik `[Save]` tanpa mengubah Position Name
13. Tunggu aksi selesai (modal tertutup)
14. Klik ikon Changelog, ketik Search `Legal Counsel {runId}-046`, tekan Enter
15. Verifikasi jumlah entri Changelog untuk `Legal Counsel {runId}-046` tetap 1 sama seperti baseline langkah 6 (tidak ada entri baru)
16. Verifikasi tidak ada entri dengan Action `Edit` untuk `Legal Counsel {runId}-046` di Changelog
17. Tutup Popup Changelog dengan `✕`
18. Buka Global Settings > Activity Log, ketik Search `Legal Counsel {runId}-046`, tekan Enter
19. Verifikasi jumlah entri Activity Log untuk `Legal Counsel {runId}-046` tetap 1 sama seperti baseline langkah 9 (tidak ada entri baru)
20. Verifikasi tidak ada entri dengan Action `Edit` untuk `Legal Counsel {runId}-046` di Activity Log

### TC-GS-POS-308: Edit No-Op tidak menghasilkan entri System Log aktor

21. Buka Global Settings > User, sub-tab User List, ketik Search email Budi Santoso, tekan Enter, buka Detail, klik tab System Log, ketik Search `Legal Counsel {runId}-046`, tekan Enter
22. Verifikasi anchor System Log: tepat 1 entri dengan Action `Create`, Object `Position`, Name `Legal Counsel {runId}-046` (baseline jumlah entri = 1)
23. Buka Global Settings > User, klik sub-tab Position, ketik Search `Legal Counsel {runId}-046` pada tabel, tekan Enter
24. Klik `⋯` pada baris `Legal Counsel {runId}-046`, pilih `Edit`
25. Klik `[Save]` tanpa mengubah Position Name
26. Tunggu aksi selesai (modal tertutup)
27. Buka Global Settings > User, sub-tab User List, ketik Search email Budi Santoso, tekan Enter, buka Detail, klik tab System Log, ketik Search `Legal Counsel {runId}-046`, tekan Enter
28. Verifikasi jumlah entri System Log untuk `Legal Counsel {runId}-046` sama seperti baseline langkah 22
29. Verifikasi System Log: tidak ada entri baru untuk `Legal Counsel {runId}-046` (tidak ada entri dengan Action `Edit`)

### TC-GS-POS-249: Position hasil Import tidak tercatat di Changelog modul

30. Buka Global Settings > User, klik sub-tab Position, klik ikon Changelog
31. Ketik Search `Legal Counsel {runId}-046`, tekan Enter
32. Verifikasi anchor Changelog: entri Create `Legal Counsel {runId}-046` tampil pada Popup Changelog yang sama
33. Ganti isi kotak search dengan `Import Probe Analyst {runId}-046`, tekan Enter
34. Verifikasi Illustration empty state tampil
35. Verifikasi Title "No results found"
36. Verifikasi Description "Try adjusting your search or filter."
37. Verifikasi tidak ada entri Create untuk `Import Probe Analyst {runId}-046`
38. Tutup Popup Changelog dengan `✕`

## Notes

- Mode: FE+BE. Sumber: `global-settings/position/TestCases/tc-position.md`. Spec ini kelas g (asersi absence): tiap TC memuat aksi nyata dan baseline sendiri. Edit No-Op dijalankan dua kali, sekali untuk TC-GS-POS-246 (Changelog dan Activity Log, langkah 10 sampai 12) dan sekali untuk TC-GS-POS-308 (System Log, langkah 23 sampai 25), masing-masing dengan baseline jumlah entri sebelum aksi.
- Pembagian TC lintas spec: TC-GS-POS-91 dan 92 (Edit No-Op pada tabel dan form) ada di spec TC-GS-POS-E2E-019, yang tidak mengklaim absence log. Pencatatan Changelog dan Activity Log untuk Create, Edit, Delete (TC-GS-POS-242 sampai 245) ada di spec TC-GS-POS-E2E-044; pencatatan System Log aktor (TC-GS-POS-251, 305, 306, 307) ada di spec TC-GS-POS-E2E-045.
- Urutan TC di spec: 246, 308, 249; TC sumber berurutan 246, 249, 308. TC-GS-POS-246 dan 308 berbagi record dan anchor dari langkah 1 sampai 3, sedangkan TC-GS-POS-249 hanya membaca Popup Changelog sehingga ditaruh terakhir.
- Anchor positif (bagian 8b konvensi): entri Create `Legal Counsel {runId}-046` dari langkah 1 sampai 3 muncul di Changelog (langkah 6, 32), Activity Log (langkah 9), dan System Log Budi Santoso (langkah 22). Anchor itu terhubung ke pemicu karena Edit No-Op berlaku pada record yang sama. Untuk TC-GS-POS-249, anchor memakai Popup Changelog yang sama dengan pencarian `Import Probe Analyst {runId}-046` (langkah 32).
- Baseline memakai jumlah entri, bukan penanda waktu, karena kolom Date log tampil pada ketelitian menit sehingga entri Create dan entri Edit yang terjadi dalam menit yang sama tidak terbedakan oleh penanda waktu.
- Langkah "Tunggu aksi selesai (modal tertutup)" (langkah 13 dan 26) ditulis tanpa `Verifikasi` sesudah `[Save]` Edit No-Op yang hasilnya tidak diasersi langsung dan langkah berikutnya pindah surface (Popup Changelog, Detail User; konvensi bagian 8b butir 8). `[Submit]` pada langkah 3 tidak diikuti langkah itu karena langkah berikutnya bekerja di tabel yang sama. Kedua langkah ini juga langkah penghubung.
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 4, 10, 23 (mencari baris target), langkah 7, 17, dan 38 (menutup Popup Changelog dengan `✕`; popup tidak dirty), serta navigasi ke surface log pada langkah 8, 18, 21, dan 27.
- Spec memuat 38 langkah (di atas smell sekitar 35 langkah). Alasan: seluruhnya satu kelas (absence log kelas g) dan satu akun; sebagian besar langkah adalah blok baca-log berpola (buka surface, Search, `Verifikasi`) yang diulang pada tiga surface log; TC-GS-POS-249 hanya membaca Popup Changelog dan ditaruh terakhir.
- Edit No-Op menutup modal otomatis (PRD FI-09) dan tidak ada dialog `Unsaved Changes`; pembukaan form Create satu kali dan Edit dua kali masing-masing berakhir dengan penutupan form (submit atau auto-close).
- Langkah 15 dan 16 (Changelog) serta 19 dan 20 (Activity Log), dan 28 dan 29 (System Log) memecah klausa "tidak ada entri baru" menjadi jumlah entri tetap sama dengan baseline dan tidak ada entri dengan Action `Edit`; klausa kedua adalah asersi tambahan di luar Expected TC-GS-POS-246 dan menjadi bukti bahwa Edit No-Op tidak tercatat sebagai Edit.
- Temuan untuk QA:
  - TC-GS-POS-246 dan 308 tidak menyebut cara membuat anchor entri log; spec membuat `Legal Counsel {runId}-046` lewat UI dan memakai entri Create-nya sebagai anchor. TC menyatakan `Legal Counsel` sudah ada; spec memakai nama bersuffix milik spec.
  - TC-GS-POS-249 precondition c (Position `Import Probe Analyst` dibuat via Import Type "Position") tidak menyebut cara pembuatannya di environment automation; spec menuliskannya sebagai seeding di hook `before` lewat jalur Import yang disediakan tim FE/BE. Kondisi bahwa Position itu berasal dari Import tidak diverifikasi spec ini.
  - TC-GS-POS-249 tidak punya Post Condition tersendiri.
  - TC-GS-POS-308 Expected "jumlah entri sama seperti sebelum Save" tidak menyebut tempat pencatatan baseline; spec mencatatnya di langkah 22.

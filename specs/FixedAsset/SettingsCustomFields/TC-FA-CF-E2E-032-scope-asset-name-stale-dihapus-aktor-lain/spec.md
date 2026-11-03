---
id: TC-FA-CF-E2E-032-scope-asset-name-stale-dihapus-aktor-lain
title: "Scope: Satu Asset Name Dihapus Aktor Lain Sebelum Submit"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-FA-CF-95
coverage:
  web: automated
---

# Scope: Satu Asset Name Dihapus Aktor Lain Sebelum Submit

## Prerequisites

- Mode: FE+BE (backend nyata).
- Akun aktor: Total Control Company Alpha (Pre-setup #1) `totalControl_automated_{namaCompany}@qwertysystem.net` (Sarah Johnson). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Custom Fields, tab General). Password lewat `Spectra.env.FA_TC_PASSWORD`; environment variable: `FA_TC_PASSWORD` (didaftarkan tim FE di `executionConfig.environmentVariables` dan `.env.example`). Password tidak ditulis di spec atau fixture.
- Pelaku kedua: sesi API Total Control sesi 2 (Pre-setup #10) `totalControlSecond_automated_{namaCompany}@qwertysystem.net` (Rina Putri) pada Company Alpha, password lewat `Spectra.env.FA_TC2_PASSWORD`; environment variable: `FA_TC2_PASSWORD` (didaftarkan tim FE). Sesi API memakai token yang tidak dihitung sebagai sesi web (dinyatakan di `suite.md`).
- Flag Guided Tooltip `guided_tooltip_seen_fa-settings-custom-fields` disetel true oleh hook `before` suite untuk akun aktor dan dipulihkan di hook `after` (dinyatakan di `suite.md`).
- Baseline Company: Company Alpha (Pre-setup #11 dan #12) dipulihkan oleh hook `before` suite (seed reset Company; nilai data mengacu `Fixture.faCustomFields.baselineGeneral`, fixture belum ada, disediakan tim FE). Spec tidak mengubah, mengedit, atau menghapus baris Pre-setup, termasuk Asset Name Pre-setup #11 (S-06).
- Data Dinamis: Asset Name `Turbine {runId}-032` pada Company Alpha, tanpa aset terkait, di-seed di hook `before` (kemampuan seeding Asset Name disediakan tim FE/BE) dan dihapus oleh sesi API pada langkah 4; Field Name `Stale One {runId}-032`, Data Type Text, Scope `Turbine {runId}-032` (hanya dipilih; field tidak pernah tersimpan).
- Kemampuan teknis: kemampuan baca System Log aktor, Activity Log, dan Modal Changelog dengan Search nama field (TC tidak menyebut path System Log dan Activity Log; disediakan tim FE); baseline nama unik bersuffix bernilai nol entri (S-12).
- Cleanup (hook `after`, tidak berasumsi UI berhasil penuh): hapus lewat API semua field dan Asset Name Company Alpha yang namanya memuat `{runId}-032` (Asset Name `Turbine {runId}-032` biasanya sudah terhapus oleh langkah 4).
- State global: tidak ada yang diubah; suite berjalan serial (`parallel: false`).

## Test Steps

### TC-FA-CF-95: Satu Asset Name yang dihapus admin lain sebelum Submit ditolak dengan pesan stale

1. Klik `[+ Custom Field]`
2. Isi Field Name `Stale One {runId}-032` dan Data Type `Text`
3. Pilih Scope `Specific Asset Name` dengan Asset Name `Turbine {runId}-032`
4. Dari sesi API Total Control sesi 2 (Pre-setup #10), hapus Asset Name `Turbine {runId}-032` di Settings > Asset Name hingga penghapusan tersimpan
5. Klik `[Submit]`
6. Verifikasi pesan inline `Turbine {runId}-032 no longer exists. Please select another.` tampil pada input Asset Name
7. Verifikasi chip `Turbine {runId}-032` dihapus dari input Asset Name
8. Verifikasi input Asset Name dikosongkan
9. Verifikasi modal tetap terbuka
10. Verifikasi input lain dipertahankan: Field Name `Stale One {runId}-032` dan Data Type `Text`
11. Klik `[✕]`
12. Verifikasi dialog `Unsaved Changes` tampil
13. Klik `[Leave]`
14. Ketik Search `Stale One {runId}-032`, tekan Enter
15. Verifikasi empty state `No results found` tampil (tidak ada field tersimpan)
16. Klik `(←)` pada kotak Search
17. Klik icon Changelog
18. Ketik Search `Stale One {runId}-032` pada Changelog, tekan Enter
19. Verifikasi Changelog tidak memuat entri untuk `Stale One {runId}-032`
20. Tutup modal Changelog
21. Buka System Log aktor
22. Ketik Search `Stale One {runId}-032`, tekan Enter
23. Verifikasi System Log aktor tidak memuat entri untuk `Stale One {runId}-032`
24. Tutup System Log aktor
25. Buka Activity Log
26. Ketik Search `Stale One {runId}-032`, tekan Enter
27. Verifikasi Activity Log tidak memuat entri untuk `Stale One {runId}-032`
28. Tutup Activity Log

## Notes

- Mode: FE+BE. Sumber: `fixed-asset/settings-custom-fields/TestCases/tc-settings-custom-fields.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Pemicu pelaku kedua memakai sesi API (bukan konteks UI kedua), ditulis 'hingga ... tersimpan' (R-20); tidak memakai `P-2` (keputusan 2026-10-30).
- P-1: klausa 'tidak ada entri log' TC-FA-CF-95 butir c tetap di spec ini karena menempel pada state stale yang dibangun alur ini (Asset Name dihapus sesi lain sebelum Submit); `Verifikasi` memakai nama field unik bersuffix (baseline nol, S-12) dan tidak ada spec absence yang memuat aksi nyata untuk TC ini (S-05).
- Langkah penghubung (aksi tanpa `Verifikasi`): penutupan form dirty pada langkah 11 dan dua langkah berikutnya (S-08); Search, membuka dan menutup Changelog, System Log aktor, dan Activity Log (R-16).
- Field Dinamis dan Asset Name Dinamis bernama bersuffix `{runId}-032` (S-12, S-06); `{runId}` hanya terdiri atas digit. Teks pesan TC `Turbine no longer exists...` ditulis dengan nama Asset Name bersuffix (`[Asset Name]` TC-FA-CF-95 butir a berisi nama Asset Name yang dipilih; R-06). Data Pre-setup hanya dibaca dan Asset Name `Turbine` Pre-setup tidak dipakai.
- Temuan untuk QA:
  - TC-FA-CF-95 butir c menyebut 'Pada langkah 7 tidak ada field tersimpan dan tidak ada entri log' tanpa menyebut path System Log aktor, Activity Log, atau cara mencari di sana; spec memakai Search nama unik dan membiarkan mekanismenya sebagai kemampuan yang disediakan tim FE.
  - TC-FA-CF-95 bertanda Manual Only (dua sesi paralel) tetapi pelaku kedua hanya memicu state; spec memakai sesi API (keputusan 2026-10-21 dan 2026-10-30).
  - TC-FA-CF-95 langkah 2 dan Data Uji menyebut Asset Name `Turbine` (Pre-setup #11); spec memakai Asset Name milik spec `Turbine {runId}-032` agar Pre-setup bersama tidak dihapus (S-06) sehingga teks pesan mengikuti nama bersuffix.

---
id: TC-AC-RP-E2E-082-tabel-approvers
title: "Tabel Approvers: Search, Filter, Sort, tanpa Download, empty filtered"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-RP-286
  - TC-AC-RP-287
  - TC-AC-RP-288
coverage:
  web: automated
---

# Tabel Approvers: Search, Filter, Sort, tanpa Download, empty filtered

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD` (nama env baru, perlu didaftarkan di `executionConfig.environmentVariables` dan `.env.example`; password tidak ditulis di spec atau fixture). Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite (`Settings > Role & Permission`, Tab Total Control aktif); hook `after` mengembalikan sesi ke akun default suite. Tidak ada ganti akun di tengah spec.
- Flag Guided Tooltip halaman ini: mengikuti pernyataan hook suite di `suite.md`.
- Suite berjalan serial (`parallel: false`); spec ini tidak bergantung pada hasil spec lain.
- Nilai data (nama user, group, role, kolom) mengacu ke fixture `fixtures/settings-role-permission.json` (belum ada; disediakan pada tahap script).
- Spec ini tidak menulis data Pre-setup; tidak ada record bersuffix `+{runId}-NNN` yang dibuat.
- Approvers `Manage allocation` `Region Jawa` = `Dewi Anggraini` (Auditor, Finance) dan `Dewi Anggreni` (QA Staff, Operations) (Pre-setup #17); Role Detail Group Role `Manage allocation` dengan node `Region Jawa` (Pre-setup #11).

## Test Steps

### TC-AC-RP-286: Search dan Filter tabel Approvers

1. Klik tab `System`
2. Pada section Group Role, klik `⋯` pada baris `Manage allocation` lalu klik `Detail`
3. Klik node `Region Jawa`
4. Klik ikon Search pada toolbar tabel Approvers
5. Verifikasi placeholder kotak Search "Search name..."
6. Ketik Search `qa`, tekan Enter
7. Verifikasi baris `Dewi Anggreni` (Position QA Staff) tampil
8. Verifikasi tidak ada baris selain `Dewi Anggreni`
9. Klik `(←)` pada kotak Search
10. Klik ikon Filter pada toolbar tabel Approvers
11. Pilih Division `Finance`
12. Klik `[Apply]`
13. Verifikasi baris `Dewi Anggraini` tampil
14. Verifikasi tidak ada baris selain `Dewi Anggraini`

### TC-AC-RP-287: Sort tabel Approvers dan tanpa Download

15. Klik `[Clear Field]`, lalu klik `[Apply]`
16. Verifikasi urutan bawaan Name A-Z
17. Klik header Name
18. Klik header Name kedua kali
19. Verifikasi urutan Name Z-A
20. Verifikasi toolbar Approvers menampilkan ikon Search dan Filter
21. Verifikasi toolbar Approvers tidak memiliki ikon Download

### TC-AC-RP-288: Empty filtered tabel Approvers

22. Ketik Search `zzz`, tekan Enter
23. Verifikasi empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah. Spec fungsional tanpa kelas harness khusus.
- Langkah penghubung (tanpa awalan Verifikasi): langkah 9 mengosongkan Search sebelum Filter (R-16); langkah 15 mengosongkan Filter sebelum TC-AC-RP-287 agar sort memiliki dua baris dengan nilai distinct (S-09, S-11).
- Search, Filter, dan Sort pada spec ini berlaku untuk tabel Approvers (bukan tabel user Role Detail) setelah node `Region Jawa` dipilih.
- Temuan untuk QA: TC-AC-RP-287 mengharapkan Name A-Z pada kondisi default dan Z-A pada klik kedua; hasil klik pertama tidak diasersi oleh TC dan tidak diasersi di spec.

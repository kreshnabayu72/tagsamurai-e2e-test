---
id: TC-AC-RP-E2E-015-empty-state-tab-dan-search-tanpa-hasil
title: "Empty State Tab Read Only, Group Manager, dan Total Control serta Search Tanpa Hasil"
priority: High
caseType: Edge
status: draft
sourceTc:
  - TC-AC-RP-60
  - TC-AC-RP-61
  - TC-AC-RP-62
  - TC-AC-RP-63
  - TC-AC-RP-64
coverage:
  web: automated
---

# Empty State Tab Read Only, Group Manager, dan Total Control serta Search Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor pertama: Default User Partner `defaultUserPartRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Wulan Sari`, entitas `Partner Mandiri`), password dari `Spectra.env.AC_RP_PART_DU_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite.
- Akun aktor kedua (ganti akun eksplisit pada langkah 9): Total Control Principal `totalControlRP_automated_{namaCompany}@qwertysystem.net` (nama tampil `Siti Nurhaliza`), password dari `Spectra.env.AC_RP_TC_PASSWORD`; akun ini juga akun default suite sehingga hook `after` mengembalikan sesi ke akun yang sama.
- Hook suite (flag Guided Tooltip, pemulihan baseline automation, sesi API aktor) dinyatakan di `suite.md`; spec ini merujuknya dan tidak mengubahnya.
- Data Pre-setup: Tabel Data Uji Pre-setup #19 (`Partner Mandiri`: Default User `Wulan Sari` satu-satunya user, tanpa Read Only, GM, maupun entri Changelog Read Only; pohon group hanya `Default Group`) dan #11 (tree group Principal) untuk Search tanpa hasil. Berkas fixture Pre-setup modul belum ada dan disediakan tim FE.
- Spec read-only: tidak membuat, mengubah, atau menghapus data; tidak ada data Dinamis, seeding, atau suffix `{runId}`. Data Pre-setup tidak diubah, jadi pemulihan baseline tidak diperlukan.
- Env var `AC_RP_PART_DU_PASSWORD` dan `AC_RP_TC_PASSWORD` adalah nama baru; keduanya harus didaftarkan di `executionConfig.environmentVariables` (`spectra.config.ts`) dan `.env.example` oleh pemilik repo e2e. Password tidak ditulis di spec atau fixture.
- Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-AC-RP-60: Tab Read Only kosong menampilkan empty state

1. Klik tab `Read Only`
2. Verifikasi tabel menampilkan Illustration dengan Title "No users assigned to this role yet." dan Description "Users assigned to this role will appear here."

### TC-AC-RP-61: Tab Group Manager kosong menampilkan empty state

3. Klik tab `Group Manager`
4. Verifikasi tabel menampilkan Title "No users assigned to this role yet." dan Description "Users assigned to this role will appear here."
5. Verifikasi Sidebar Group Tree tetap tampil

### TC-AC-RP-62: Tab Total Control tidak pernah kosong

6. Klik tab `Total Control`
7. Verifikasi tabel Tab Total Control menampilkan baris Default User entitas (`Wulan Sari`)
8. Verifikasi empty state tidak tampil

### TC-AC-RP-63: Search tanpa hasil pada Tab Total Control

9. Logout dari akun `Wulan Sari`
10. Login sebagai `Siti Nurhaliza` (Total Control Principal) dengan password dari `Spectra.env.AC_RP_TC_PASSWORD`
11. Buka halaman `Settings > Role & Permission` lewat menu Settings di sidebar
12. Klik ikon Search, ketik Search "zzz", tekan Enter
13. Verifikasi tabel menampilkan empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
14. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

### TC-AC-RP-64: Search tanpa hasil pada Tab System

15. Klik tab `System`
16. Klik ikon Search, ketik Search "zzz", tekan Enter
17. Verifikasi section Global Role menampilkan empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
18. Verifikasi section Group Role menampilkan empty state dengan Title "No results found" dan Description "Try adjusting your search or filter."
19. Klik `(←)` pada kotak Search untuk menutup input dan mereset tabel

## Notes

- Mode: FE+BE. Sumber: `admin-console/settings-role-permission/TestCases/tc-settings-role-permission.md`. Seluruh TC spec ini TC FE; spec tanpa kelas harness khusus.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Ganti akun eksplisit pada langkah 9: TC-AC-RP-60 sampai TC-AC-RP-62 mensyaratkan Default User entitas Partner, TC-AC-RP-63 dan TC-AC-RP-64 mensyaratkan Total Control entitas Principal (Search "zzz" harus berasal dari data Principal). Login dan pembukaan halaman sesudahnya adalah langkah penghubung ganti akun (S-07).
- Langkah penghubung tanpa awalan Verifikasi (S-03): langkah 14 dan 19 mengosongkan Search dengan klik `(←)` pengganti frasa "Kosongkan Search" (R-16, 8b butir 9); Search "zzz" adalah langkah TC sumber.
- Empty state "No results found" yang diproses Search adalah anchor positif yang sah untuk hasil Search kosong (8b butir 2); Tab Total Control pada TC-AC-RP-62 mengasersi baris Default User sebagai pembanding bahwa tabel bukan empty state.
- Temuan untuk QA:
  - TC-AC-RP-60 menyebut Illustration pada empty state, sedangkan TC-AC-RP-61 dan TC-AC-RP-23 tidak menyebut Illustration; asersi mengikuti Expected tiap TC.
  - TC-AC-RP-62 Expected menulis "minimal menampilkan baris Default User entitas"; spec mengasersi baris `Wulan Sari` (Default User Partner Mandiri, Pre-setup #19).
  - TC-AC-RP-64 Expected "Kedua section menampilkan ... Search tanpa hasil" tidak menyatakan apakah Pagination atau toolbar berubah; hanya empty state kedua section yang diasersi.

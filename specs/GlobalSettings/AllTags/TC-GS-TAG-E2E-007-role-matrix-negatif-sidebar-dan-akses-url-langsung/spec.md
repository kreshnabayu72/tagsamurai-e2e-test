---
id: TC-GS-TAG-E2E-007-role-matrix-negatif-sidebar-dan-akses-url-langsung
title: "Role Matrix Negatif: Menu TAG Tidak Tampil di Sidebar dan Akses URL Registri Langsung Ditolak"
priority: High
caseType: Negative
status: draft
sourceTc:
  - TC-GS-TAG-29
  - TC-GS-TAG-30
coverage:
  web: automated
---

# Role Matrix Negatif: Menu TAG Tidak Tampil di Sidebar dan Akses URL Registri Langsung Ditolak

## Prerequisites

- Mode: FE+BE.
- Akun aktor: lihat tabel "Role yang diuji" di bawah. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite (Total Control, `GS_TC_PASSWORD`).

Role yang diuji (Tabel Data Uji Pre-setup; Client A):

| TC | Role | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-29, TC-30 | Tanpa Kapabilitas (tanpa capability Manage TAG dan tanpa Manage asset & TAG di FAMS, bukan Total Control atau Read Only) | Rina Marlina | `noCapability_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_NOCAP_PASSWORD` |

- Data: spec tidak membuat, mengubah, atau menghapus data; hanya visibilitas menu dan hasil akses URL yang diperiksa. URL halaman Global Settings > TAG dirujuk dari fixture `Fixture.allTags.url` (fixture dibuat tahap script).
- Layar awal: Beranda Global Settings dibuka di hook `beforeEach`.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- State global: tidak ada yang diubah. Capability akun adalah data Pre-setup. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-29: Tanpa kapabilitas Manage TAG: menu TAG tidak tampil di sidebar

1. Amati sidebar Global Settings sebagai Rina Marlina
2. Verifikasi sedikitnya satu item menu Global Settings lain tampil di sidebar
3. Verifikasi item `TAG` tidak tampil pada sidebar

### TC-GS-TAG-30: Tanpa kapabilitas membuka URL registri langsung ditolak

4. Ketik atau paste URL halaman Global Settings > TAG langsung di address bar, lalu tekan Enter
5. Verifikasi toast error `You don't have permission to do this.`
6. Verifikasi tidak ada redirect ke halaman unauthorized
7. Verifikasi daftar tag tidak termuat

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 2). Subjudul `###` memetakan langkah ke id TC granular. Role Matrix negatif mengikuti bagian 3a: sidebar tersembunyi dan akses URL langsung adalah spec negatif tersendiri.
- Langkah 2 adalah anchor positif untuk absence menu pada langkah 3 (8b butir 2); TC-29 tidak menyebut item menu lain yang tampil, spec memakai sedikitnya satu item menu Global Settings yang dapat diakses akun itu. Langkah 5 menjadi anchor untuk langkah 7 (tidak ada daftar tag).
- Temuan untuk QA:
  - TC-30 menyebut "URL halaman Global Settings > TAG" tanpa menuliskan URL; spec merujuk fixture `Fixture.allTags.url` (S-13).
  - TC-30 Expected b ("tidak ada redirect ke halaman unauthorized") tidak merinci halaman yang tampil setelah toast; spec hanya mengasersi tidak ada redirect dan daftar tag tidak termuat.
  - Post Condition kedua TC bernilai `-`.

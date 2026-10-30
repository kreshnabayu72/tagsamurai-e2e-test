---
id: TC-GS-DIV-E2E-054-changelog-empty-state
title: "Modal Changelog: Empty State Belum Ada Riwayat dan Search Tanpa Hasil"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-DIV-191
  - TC-GS-DIV-192
coverage:
  web: automated
---

# Modal Changelog: Empty State Belum Ada Riwayat dan Search Tanpa Hasil

## Prerequisites

- Mode: FE+BE.
- Akun aktor 1 (awal spec): Total Control Client A, Sari Dewi (`Sari D`), `totalControl_automated_qaTeam1@qwertysystem.net` (Tabel Data Uji Pre-setup baris 1), kredensial `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`. Dipakai untuk TC-GS-DIV-192.
- Akun aktor 2 (ganti akun di langkah 7 dan 8): Total Control Client C, Rudi Hartanto, `totalControl_automated_qaTeam3@qwertysystem.net`, kredensial `Spectra.env.GS_CLIENTC_TC_PASSWORD`. Dipakai untuk TC-GS-DIV-191. Akun dan entitas ini tidak ada di Tabel Data Uji Pre-setup Division; nama akun, email, dan env var mengikuti suite Brand dan disediakan tim FE. Entitas ini tidak boleh memiliki entri Changelog Division sama sekali (tidak ada seeding Division di Client C).
- Environment variable: `GS_TC_PASSWORD`, `GS_CLIENTC_TC_PASSWORD`. Password tidak ditulis di spec atau fixture.
- Seeding (lewat API oleh akun Sari Dewi di hook `before`): Division `Log Seed Div {runId}-054` dibuat sehingga Changelog Client A memiliki sedikitnya satu entri (Action Create oleh `Sari D`); precondition TC-GS-DIV-192 mensyaratkan riwayat terisi supaya Search `zzzzqq` menghasilkan `No results found`, bukan `No changelog yet`.
- Cleanup (hook `after`, tidak berasumsi seeding berhasil penuh): hapus `Log Seed Div {runId}-054` lewat API; kembalikan sesi ke akun default suite (Total Control Client A, `GS_TC_PASSWORD`) karena spec berakhir di Client C. Entri Changelog tidak bisa dihapus.
- Kemampuan teknis: logout lalu login ulang pada browser yang sama (langkah 7 dan 8).
- Precondition TC-GS-DIV-191: login sebagai Total Control, berada di Global Settings > User > Division, entitas tanpa riwayat Changelog Division. TC-GS-DIV-192: riwayat Changelog Division terisi.
- Flag Guided Tooltip `guided_tooltip_seen_gs-division`: diatur hook suite (lihat `suite.md`, bagian Hook suite); spec ini tidak mengatur flag sendiri.
- State global yang dipulihkan: sesi login (di hook `after`, lihat Cleanup).

## Test Steps

### TC-GS-DIV-192: Empty state Modal Changelog saat Search tidak menemukan hasil

1. Klik icon Changelog di Table Tools
2. Ketik Search `zzzzqq` di modal, tekan Enter
3. Verifikasi Illustration (100x100) tampil
4. Verifikasi Title `No results found`
5. Verifikasi Description `Try adjusting your search or filter.`
6. Klik icon `[✕]` untuk menutup Modal Changelog

### Ganti akun ke Client C

7. Logout dari Total Control Client A
8. Login sebagai Total Control Client C

### TC-GS-DIV-191: Empty state Modal Changelog saat belum ada riwayat

9. Buka Global Settings > User > Division
10. Klik icon Changelog di Table Tools
11. Verifikasi Illustration (100x100) tampil
12. Verifikasi Title `No changelog yet`
13. Verifikasi Description `Activities and changes will appear here.`

## Notes

- Mode: FE+BE. Sumber: `global-settings/division/TestCases/tc-division.md`.
- Subjudul `###` memetakan langkah ke id TC granular untuk report per langkah.
- Urutan TC dalam spec: TC-GS-DIV-192 (Client A) lebih dulu, lalu TC-GS-DIV-191 (Client C), supaya semua TC Client A selesai sebelum ganti akun. Bagian Client C tetap bermakna walau bagian Client A gagal (ada langkah ganti akun eksplisit).
- Langkah penghubung (aksi tanpa `Verifikasi`): langkah 6 (menutup Modal Changelog), langkah 7 dan 8 (ganti akun ke Client C), langkah 9 (membuka tab Division di Client C).
- Temuan untuk QA: (1) TC-GS-DIV-191 precondition "Entitas tanpa riwayat Changelog Division sama sekali" tidak menyebut entitas atau akunnya; Tabel Data Uji Pre-setup Division tidak memuatnya, spec memakai akun Client C dari suite Brand dan menyatakannya disediakan tim FE. (2) Tidak diketahui apakah Division Pre-setup Client C ada; spec mensyaratkan Client C tanpa entri Changelog Division.

---
id: TC-GS-TAG-E2E-004-empty-state-dan-error-load-registri
title: "Empty State S-01/S-02/S-03 pada Client Tanpa Tag dan Semua Paired, serta Error Load dengan Try Again"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-18
  - TC-GS-TAG-19
  - TC-GS-TAG-20
  - TC-GS-TAG-22
coverage:
  web: automated
---

# Empty State S-01/S-02/S-03 pada Client Tanpa Tag dan Semua Paired, serta Error Load dengan Try Again

## Prerequisites

- Mode: FE+BE (TC-22 memakai intercept parsial di atas backend nyata).
- Akun aktor (password lewat `Spectra.env`, tidak ditulis di spec atau fixture):

| TC | Client | Nama user | Email | Env var password |
|---|---|---|---|---|
| TC-18, TC-19 | Client Empty | Budi Santoso | `totalControl_automated_qaEmpty@qwertysystem.net` | `Spectra.env.GS_TC_EMPTY_PASSWORD` |
| TC-20 | Client AllPaired | Siti Rahmawati | `totalControl_automated_qaAllPaired@qwertysystem.net` | `Spectra.env.GS_TC_ALLPAIRED_PASSWORD` |
| TC-22 | Client A | Sari Dewi | `totalControl_automated_qaTeam1@qwertysystem.net` | `Spectra.env.GS_TC_PASSWORD` |

- Login akun pertama (Client Empty) di hook `before`; ganti akun ke Client AllPaired dan Client A ditulis sebagai langkah (langkah 15 sampai 16 dan 22 sampai 23). Hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Client Empty tanpa tag dan tanpa riwayat (plan Growth); Client AllPaired punya tag dan seluruhnya Paired; Client A memuat Seed Registri A (DD-01 s.d. DD-30), di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Kebutuhan intercept (`Spectra.intercept()` di atas backend nyata, disediakan tim FE): respons 5xx untuk request daftar registri TAG; dipasang pada langkah 25 dan dilepas pada langkah 32 (segera setelah pemicu). Nama endpoint konkret ditentukan tim FE dari `openapi.yaml` di tahap script.
- Layar awal: Global Settings > TAG Tab All dibuka di hook `beforeEach` untuk akun hook; setelah ganti akun, halaman dibuka lewat langkah.
- Guided Tooltip: flag `guided_tooltip_seen_gs-tag-registry` disetel true untuk ketiga akun oleh hook suite `before` dan dipulihkan di `after` (pernyataan hook di `suite.md`); spec ini tidak mengubahnya.
- Selektor: ilustrasi empty state belum punya ID/aria-label dan bentuknya tidak ditetapkan sumber (PRD §7.1 tidak menyebut ilustrasi); selektor disediakan tim FE di tahap script.
- State global: tidak ada yang diubah. Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-18: Empty state S-01 pada Tab All dan Tab Not Paired saat registri belum punya tag

1. Amati area tabel Tab All
2. Verifikasi ilustrasi empty state tampil
3. Verifikasi judul `No TAGs found`
4. Verifikasi deskripsi `There are no TAGs activated in your organization yet.`
5. Verifikasi tidak ada tombol aksi pada empty state
6. Klik Tab Not Paired
7. Verifikasi ilustrasi empty state tampil
8. Verifikasi judul `No TAGs found`
9. Verifikasi deskripsi `There are no TAGs activated in your organization yet.`
10. Verifikasi tidak ada tombol aksi pada empty state

### TC-GS-TAG-19: Empty state S-02 pada Tab Paired saat belum ada tag tertaut

11. Klik Tab Paired
12. Verifikasi judul `No paired TAGs`
13. Verifikasi deskripsi `TAGs will appear here once they are paired to assets or users.`
14. Verifikasi tidak ada tombol aksi pada empty state

### TC-GS-TAG-20: Empty state S-03 pada Tab Not Paired saat seluruh tag berstatus Paired

15. Logout dari akun Client Empty
16. Login sebagai Total Control Client AllPaired
17. Buka Global Settings > TAG
18. Klik Tab Not Paired
19. Verifikasi judul `No available TAGs`
20. Verifikasi deskripsi `All active TAGs are currently paired. Activate new TAGs to expand your pool.`
21. Verifikasi tidak ada tombol aksi pada empty state

### TC-GS-TAG-22: Gagal memuat registri menampilkan error state dengan Try Again, bukan empty state

22. Logout dari akun Client AllPaired
23. Login sebagai Total Control Client A
24. Buka Global Settings > TAG > Tab All
25. Pasang intercept respons 5xx untuk request daftar registri TAG
26. Muat ulang halaman Global Settings > TAG
27. Amati area tabel
28. Verifikasi area tabel menampilkan `Unable to load this data.`
29. Verifikasi tombol `Try Again` tampil
30. Verifikasi tidak ada toast
31. Verifikasi area tabel bukan empty state
32. Lepas intercept
33. Klik `Try Again`
34. Verifikasi tabel memuat baris Seed Registri A

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1d). Subjudul `###` memetakan langkah ke id TC granular.
- Pengecualian P-5: TC-22 (kegagalan 5xx pada pembacaan registri) adalah satu-satunya objek-uji ringan kelas b di spec ini dan berada di spec empty state/error karena permukaan dan layar yang sama. Intercept dilepas segera setelah pemicu (langkah 32).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 1, 6, 11, 17, 18, 24, 27 (membuka/mengamati), ganti akun langkah 15, 16, 22, 23 (S-07, eksplisit). Langkah 30 (tidak ada toast) dan 31 (bukan empty state) memakai langkah 28 dan 29 sebagai anchor positif (8b butir 2). Langkah 2 dan 7 (`Verifikasi` ilustrasi) mengasersi klausa "ilustrasi" pada Expected TC-18 a dan b; selektor ilustrasi disediakan tim FE.
- Temuan untuk QA:
  - TC-18 butir a menyebut tombol `+ Activate TAG` hanya ada di toolbar; spec mengasersi hanya tidak ada tombol aksi pada empty state (tombol toolbar tidak diasersi di spec ini).
  - TC-18 butir a menyebut "ilustrasi" pada empty state, tetapi PRD §7.1 tidak menyebut ilustrasi dan bentuknya tidak ditetapkan; spec mengasersi ilustrasi tampil (langkah 2 dan 7) dan selektornya disediakan tim FE.
  - TC-18 sampai TC-20 tidak menyebut nilai Table Tools yang tampil pada empty state; tidak diasersi.
  - TC-21 (Search tanpa hasil, `No results found`) ada di spec 066 (Search registri), bukan di spec ini.
  - Post Condition semua TC bernilai `-`.

---
id: TC-GS-TAG-E2E-005-guided-tooltip-registri-konten-navigasi-dan-flag-seen
title: "Guided Tooltip Registri: Empat Step, Done, Skip, Back Tersembunyi, Replay [?], dan Flag Seen"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-TAG-23
  - TC-GS-TAG-24
coverage:
  web: automated
---

# Guided Tooltip Registri: Empat Step, Done, Skip, Back Tersembunyi, Replay [?], dan Flag Seen

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control Client A (Sari Dewi) `totalControl_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before`; hook `after` mengembalikan sesi ke akun default suite.
- Data Pre-setup (hanya dibaca): Seed Registri A (DD-01 s.d. DD-30), plan Growth. Seed di-seed ulang idempotent oleh hook `before` (Q-4; mekanisme disediakan tim FE/BE).
- Guided Tooltip (page_key `gs-tag-registry`): spec ini menguji flag `guided_tooltip_seen_gs-tag-registry` sendiri sehingga dikecualikan dari penyetelan true oleh hook suite `before` (lihat `suite.md`). Hook `before` mencatat nilai awal flag akun Total Control lalu mereset flag ke belum ada (precondition "flag seen belum true" TC-23 dan TC-24). Flag direset lagi sebagai langkah penghubung sebelum TC-24 karena TC-23 menandainya seen. Hook `after` memulihkan nilai awal flag. Mekanisme baca, reset, dan pemulihan flag disediakan tim FE/BE (tidak didefinisikan di TC, PRD, atau LLD).
- Layar awal: kunjungan pertama ke halaman adalah pemicu auto-open Guided Tooltip, sehingga langkah buka ditulis di `## Test Steps` dan bukan di hook `beforeEach`.
- Selektor: PRD menetapkan target step (`#license-counter-cards`, `#tag-tabs`, `#tag-table-toolbar`, `#btn-filter`); selektor tombol tooltip dan ikon `[?]` belum ada di sumber dan diselesaikan tim FE di tahap script.
- State global: hanya flag Guided Tooltip (dipulihkan seperti di atas). Suite berjalan serial (`parallel: false`).

## Test Steps

### TC-GS-TAG-23: Guided tooltip registri muncul otomatis pada kunjungan pertama dengan empat step

1. Buka Global Settings > TAG
2. Amati tooltip step pertama
3. Verifikasi Step 1 Title `License Counter`
4. Verifikasi Step 1 Description `Monitor your license quota balance and TAG health for each TAG type.`
5. Verifikasi Step 1 menyorot elemen target yang terlihat
6. Klik `Next`
7. Verifikasi Step 2 Title `TAG Tabs`
8. Verifikasi Step 2 Description `Switch tabs to filter the TAG list by pairing state.`
9. Verifikasi Step 2 menyorot elemen target yang terlihat
10. Klik `Next`
11. Verifikasi Step 3 Title `TAG Actions`
12. Verifikasi Step 3 Description `Run actions on TAGs in the field and review session history — available actions depend on your access level.`
13. Verifikasi Step 3 menyorot elemen target yang terlihat
14. Klik `Next`
15. Verifikasi Step 4 Title `Search & Filter`
16. Verifikasi Step 4 Description `Find TAGs by code, status, or other attributes.`
17. Verifikasi Step 4 menyorot elemen target yang terlihat
18. Verifikasi Step 4 menampilkan tombol `Done`
19. Verifikasi Step 4 tidak menampilkan tombol `Next`
20. Klik `Done`
21. Verifikasi tur tertutup
22. Verifikasi flag seen tersimpan (dibaca lewat kemampuan baca flag yang disediakan tim FE/BE)

### TC-GS-TAG-24: Navigasi guided tooltip registri: Skip, Back tersembunyi di Step 1, replay tidak mereset flag

23. Reset flag `guided_tooltip_seen_gs-tag-registry` akun Total Control ke belum ada (langkah penghubung)
24. Muat ulang halaman Global Settings > TAG
25. Amati tombol pada Step 1
26. Verifikasi tombol `Skip` tampil pada Step 1
27. Verifikasi tombol `Next` tampil pada Step 1
28. Verifikasi tombol `Back` Hidden pada Step 1
29. Klik `Next`
30. Klik `Back`
31. Verifikasi tooltip kembali ke Step 1
32. Klik `Skip`
33. Verifikasi tur tertutup
34. Verifikasi flag seen tersimpan
35. Muat ulang halaman
36. Verifikasi Tab `All`, `Paired`, `Not Paired` tampil
37. Verifikasi tur tidak muncul otomatis
38. Hover ikon `[?]` di kanan Breadcrumb
39. Verifikasi tooltip `Show guide`
40. Klik ikon `[?]` di kanan Breadcrumb
41. Verifikasi tur dimulai dari Step 1
42. Verifikasi flag seen tidak direset (tetap true)
43. Tutup tur dengan klik `Skip` (langkah penghubung)

## Notes

- Mode: FE+BE. Sumber: `global-settings/all-tags/TestCases/tc-all-tags.md` (Section 1e). Subjudul `###` memetakan langkah ke id TC granular.
- Spec ini mengatur flag sendiri sebagai pengecualian pernyataan hook di `suite.md` (flag `gs-tag-registry`).
- Langkah penghubung (tanpa `Verifikasi`, S-03): langkah 23 (reset flag), 24 (muat ulang untuk memicu auto-open), 43 (menutup tur agar tidak membekas). Langkah 26 dan 27 adalah anchor positif untuk langkah 28 (absence `Back`, 8b butir 2). Langkah 36 adalah anchor positif untuk langkah 37 (absence tur tidak muncul, 8b butir 2). Langkah 31 memverifikasi hasil `Back` (TC langkah 3 menyebut Next lalu Back tanpa Expected tersendiri; asersi tambahan ini dicatat karena hasil Back perlu teramati).
- Alasan spec melewati sekitar 35 langkah (43): dua TC Guided Tooltip pada satu halaman dan satu akun; langkah terbanyak adalah `Verifikasi` Title dan Description tiap dari empat step (S-01, satu per klausa).
- Temuan untuk QA:
  - TC-23 butir e ("target elemen permanen") tidak menyebut pemetaan step ke elemen target; spec hanya mengasersi step menyorot elemen yang terlihat tanpa selektor (PRD menetapkan target `#license-counter-cards`, `#tag-tabs`, `#tag-table-toolbar`, `#btn-filter` tanpa pemetaan per step di TC).
  - TC-23 Post Condition dan Expected f ("flag seen tersimpan") tidak memberi langkah observasi di UI; spec memakai kemampuan baca flag disediakan tim FE/BE (S-11) hanya untuk butir Expected.
  - Post Condition kedua TC bernilai `-`.

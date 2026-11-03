---
id: TC-FA-RP-E2E-218-modal-changelog-search-dan-filter-1
title: "Modal Changelog: Search dan Filter (1/6)"
priority: Critical
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-709
  - TC-FA-RP-710
coverage:
  web: automated
---

# Modal Changelog: Search dan Filter (1/6)

## Prerequisites

- Mode: FE+BE
- Akun: Total Control (Pre-setup #2, Siti Rahmawati, `totalControl_automated_{namaCompany}@qwertysystem.net`), `Spectra.env.FA_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite pada tab awal Total Control.
- Flag Guided Tooltip, sesi API aktor, dan pemulihan Pre-setup bersama mengikuti pernyataan "Hook suite" di `suite.md`.
- Data Pre-setup (identitas dirujuk lewat `Fixture.fixedAssetRolePermission.<kunci>`; berkas fixture belum ada dan disediakan tim FE): #42 (Changelog Tab Total Control, enam entri seed, urutan seeding dari terlama ke terbaru: Assign Rina Wulandari (`—` ke `Total Control`, Modified By `Siti R`); Assign Ahmad Fauzi (`—` ke `Total Control`, `Siti R`); Assign Budi Santoso (`—` ke `Total Control`, `Prasetyo H`); Remove Budi Santoso (`Total Control` ke `—`, `Rina W`); Auto-Revert Fitri Handayani (`Total Control` ke `—`, `Siti R`); Assign Maya Anggraeni (`Read Only` ke `Total Control`, `Rina W`); seluruh entri Field `Access Level`). Pre-setup #24 disebut Precondition TC dan dipakai sebagai precondition TC, tidak diasersi. Entri seed #42 ditambahkan fixture backend yang disediakan tim FE/BE di hook `before`. Changelog adalah audit trail permanen (S-12): spec tidak mengasumsikan total entri tetap; entri seed dikenali lewat kombinasi Action, User Name, Old Value, dan New Value, dan total pada info pagination dibandingkan dengan baseline yang dicatat di langkah spec. Spec ini tidak mengubah data.

## Test Steps

### Screening Modal Changelog Tab Total Control (TC 709)

1. Klik ikon Changelog pada toolbar.
2. Catat total entri pada info pagination sebagai baseline.
3. Verifikasi Title modal `Changelog: Role & Permission > Total Control`.
4. Klik ikon Search pada toolbar modal.
5. Verifikasi toolbar memuat `Search`, `Filter`, dan `Download`.
6. Verifikasi placeholder Search `Search action, user, or value...`.
7. Klik ikon `(←)` pada kotak Search.
8. Verifikasi kolom tabel: `Date (sortable)`, `Action (sortable)`, `User Name (sortable)`, `Field (sortable)`, `Old Value (sortable)`, `New Value (sortable)`, `Modified By (sortable)`, `Column Visibility (⋯)`.
9. Verifikasi tidak ada row action.
10. Verifikasi urutan default Date descending.
11. Verifikasi entri seed Pre-setup #42 tampil dengan urutan relatif Date descending: Assign Maya Anggraeni (`Read Only` ke `Total Control`), Auto-Revert Fitri Handayani (`Total Control` ke `—`), Remove Budi Santoso (`Total Control` ke `—`), Assign Budi Santoso (`—` ke `Total Control`), Assign Ahmad Fauzi (`—` ke `Total Control`), Assign Rina Wulandari (`—` ke `Total Control`), diidentifikasi lewat kombinasi Action, User Name, Old Value, dan New Value.
12. Verifikasi total pada info pagination sama dengan baseline langkah 2.
13. Verifikasi pagination default 10 data per halaman.

### Siklus interaksi Search toolbar (TC 710)

14. Arahkan kursor ke ikon Search di toolbar.
15. Verifikasi tooltip `Search`.
16. Klik ikon Search.
17. Verifikasi kotak Search melebar.
18. Verifikasi kursor otomatis fokus di input.
19. Verifikasi placeholder input `Search action, user, or value...`.
20. Ketik `auto` pada input Search tanpa menekan Enter.
21. Verifikasi ikon `(✕)` muncul di dalam input.
22. Verifikasi tabel belum tersaring: total pada info pagination masih sama dengan baseline langkah 2.
23. Tekan Enter.
24. Verifikasi tabel tersaring: hanya entri Auto-Revert Fitri Handayani yang tampil.
25. Klik ikon `(✕)` pada kotak Search.
26. Verifikasi teks input terhapus.
27. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus.
28. Verifikasi tabel tetap menampilkan hasil pencarian terakhir: hanya entri Auto-Revert Fitri Handayani.
29. Tekan Enter pada input kosong.
30. Verifikasi tabel kembali menampilkan seluruh data: total pada info pagination sama dengan baseline langkah 2.
31. Ketik Search `auto`, tekan Enter.
32. Klik ikon `(←)`.
33. Verifikasi kotak Search menutup dan keyword dikosongkan.
34. Verifikasi tabel langsung kembali menampilkan seluruh data: total pada info pagination sama dengan baseline langkah 2.

## Notes

- Langkah penghubung (S-03): langkah 2 (mencatat total entri sebagai baseline, sesuai TC 709 langkah 3; dibandingkan pada langkah 12, 22, 30, dan 34), serta langkah 4 dan 7 (membuka lalu menutup input Search agar placeholder pada Expected TC 709 butir a dapat diamati).
- Halaman dan Tab `Total Control` dibuka hook `beforeEach` suite, sehingga langkah TC `Klik Tab Total Control` tidak diulang di Test Steps.
- Temuan untuk QA:
  - TC 709 butir a menyebut placeholder Search pada toolbar tanpa langkah membuka kotak Search; spec menambah langkah penghubung 4 dan 7.
  - TC 710 butir a menyebut placeholder pada Langkah 3 (hover), padahal input baru terbuka pada Langkah 4; placeholder diasersi pada langkah 19 setelah input terbuka (S-14).
  - Precondition TC 709 dan 710 menyebut Pre-setup #42 (enam entri seed Tab Total Control) bersama #24 (Company Changelog, 25 entri); spec memakai aktor Total Control #2 dengan data #42.

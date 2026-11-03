---
id: TC-AC-ACC-E2E-059-create-dan-edit-peran-group-manager-tree-descendant
title: "Group Manager: Create dan Edit Client di Node Descendant dengan Tree Select Group"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-ACC-124
  - TC-AC-ACC-585
  - TC-AC-ACC-541
  - TC-AC-ACC-587
coverage:
  web: automated
---

# Group Manager: Create dan Edit Client di Node Descendant dengan Tree Select Group

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Group Manager Area Jakarta + descendant (A-03) `groupManagerJakarta_automated_qaTeam1@qwertysystem.net`, password `Spectra.env.AC_CLIENT_GM_PASSWORD`. Login akun Group Manager Area Jakarta + descendant di hook `before` spec ini; halaman Admin Console > Client dibuka hook `beforeEach` suite. Hook `after` mengembalikan sesi ke akun default suite. Env var password didaftarkan di `executionConfig.environmentVariables` dan `.env.example` saat tahap script.
- Data Pre-setup (Tabel A: C-01…C-14, Group tree baseline, aktor A-01…A-16) tersedia dan hanya dibaca; spec tidak mengubahnya.
- Data valid Create (kecuali bila kasus menyebut lain): PIC Name `Rina Kartika`; PIC Email `rina.kartika@qwertysystem.net`; Address `Jl. Sudirman No. 10`; Country/State/City `Indonesia`/`DKI Jakarta`/`Jakarta Selatan`; Postal Code `12190`; Default User First Name, Last Name, Email (`<nama>+{runId}-059@qwertysystem.net`, unik per run), Division `Finance`; Position kosong; Select Group `Area Jakarta` bila Partner kosong. Default User untuk TC-585: `Agus Setiawan`, Division `Operasional`, PIC Email `rina.kartika.mtb+{runId}-059@qwertysystem.net`.
- Dataset Dinamis: `PT Menteng Baru {runId}-059` (dibuat UI). Dataset seed: Client `PT Menteng Edit {runId}-059` (setara C-ROL-16: Direct, Group Cabang Menteng, Fax kosong, Default User Not Yet Activated). Seeding Client lewat API/fixture BE di hook `before` (kemampuan disediakan tim FE/BE; endpoint tidak dikarang).
- Cleanup: hook `after` menghapus lewat API (soft-delete) Client yang dibuat atau di-seed spec ini, tanpa mengasumsikan setup berhasil penuh.
- Suite berjalan serial (`parallel: false`); flag Guided Tooltip halaman Client disetel oleh hook suite (`suite.md`).

## Test Steps

### TC-124 dan TC-585: Create di node descendant

1. Klik `[+ New Client]`
2. Biarkan field Partner kosong
3. Buka tree Select Group
4. Verifikasi "Area Jakarta" dan "Cabang Menteng" dapat dipilih
5. Verifikasi "Regional Barat" greyed out
6. Verifikasi "Cabang Bekasi", "Regional Timur", "Area Surabaya", dan "Cabang Rungkut" tidak muncul (hidden)
7. Isi Company Name `PT Menteng Baru {runId}-059`, PIC Name, PIC Email, Address, Country, State, City, Postal Code, Default User First Name, Last Name, Email, dan Division sesuai Data valid Create; Default User Agus Setiawan dengan Email `agus.setiawan+{runId}-059@qwertysystem.net`, Division `Operasional`, PIC Email `rina.kartika.mtb+{runId}-059@qwertysystem.net`, Select Group dikosongkan
8. Pilih node "Cabang Menteng" pada tree Select Group
9. Klik `[Submit]`
10. Verifikasi popup tertutup
11. Verifikasi toast sukses "Success, client has been created."
12. Ketik Search `PT Menteng Baru {runId}-059`, tekan Enter
13. Verifikasi baris "PT Menteng Baru {runId}-059" muncul di sub-tab Active dengan Managed By "Direct"
14. Verifikasi baris "PT Menteng Baru {runId}-059": Group "Cabang Menteng"

### TC-541 dan TC-587: Edit Client Direct di node descendant

15. Ketik Search `PT Menteng Edit {runId}-059`, tekan Enter
16. Buka `⋯` baris `PT Menteng Edit {runId}-059` lalu klik `Edit`
17. Verifikasi popup dengan Title "Edit Client" terbuka
18. Verifikasi field Select Group terisi "Cabang Menteng"
19. Buka tree Select Group
20. Verifikasi "Area Jakarta" dan "Cabang Menteng" dapat dipilih
21. Verifikasi "Regional Barat" greyed out (tidak dapat dipilih)
22. Verifikasi "Regional Timur" dan "Area Surabaya" tidak tampil
23. Pilih node "Cabang Menteng" (menutup tree tanpa mengubah Group)
24. Isi Fax dengan `0215550143`
25. Klik `[Save]`
26. Verifikasi popup tertutup
27. Verifikasi toast sukses "Success, client has been updated."
28. Klik Company Name `PT Menteng Edit {runId}-059` untuk membuka Detail
29. Verifikasi Detail menampilkan Fax "0215550143"

## Notes

- Subjudul `###` memetakan langkah ke id TC granular; `TC-n` berarti `TC-AC-ACC-n`.
- Langkah penghubung (S-03): "Pilih node Cabang Menteng" menutup tree tanpa mengubah nilai sebelum mengisi Fax (TC-541 dan TC-587 berbagi popup Edit); Search nama unik.
- Verifikasi baris List TC-585 dilakukan sesudah popup tertutup. Cleanup menghapus kedua Client lewat hook `after`.
- Temuan untuk QA:
  - Post Condition TC-585 (Default User tanpa App Access dan tanpa Activation Email; Changelog Create tercatat) dan TC-587 (Changelog `Edit` Field `Fax` tercatat) tidak punya langkah observasi di TC; tidak diasersi.

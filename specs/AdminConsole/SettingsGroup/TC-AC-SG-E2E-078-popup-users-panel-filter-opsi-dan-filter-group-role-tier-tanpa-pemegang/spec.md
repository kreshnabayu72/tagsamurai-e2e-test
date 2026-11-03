---
id: TC-AC-SG-E2E-078-popup-users-panel-filter-opsi-dan-filter-group-role-tier-tanpa-pemegang
title: "Popup Users: Panel Filter, Opsi dan Filter Group Role, dan Tier Tanpa Pemegang"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-AC-SG-285
  - TC-AC-SG-286
  - TC-AC-SG-287
  - TC-AC-SG-288
  - TC-AC-SG-289
coverage:
  web: automated
---

# Popup Users: Panel Filter, Opsi dan Filter Group Role, dan Tier Tanpa Pemegang

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control entitas Principal (Pre-setup #1) `totalControlGroup_automated_{namaCompany}@qwertysystem.net` (nama tampil `Budi Santoso`), password `Spectra.env.AC_TC_PASSWORD`.
- Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite. Hook `after` memulihkan sesi ke akun default spec.
- Flag Guided Tooltip halaman Settings > Group disetel `seen` oleh hook suite (lihat `suite.md`); spec ini tidak mengubahnya.
- Data Pre-setup (dibaca saja, tidak ditulis spec ini): entitas Principal `Pohon Uji Utama` (Pre-setup #16, 14 group), Total User per node (#17), penugasan Group Role dan Group Manager (#18). Node `Region A`: Total User 5 (`Budi Santoso` Total Control, `Rina Wijaya` Read Only, `Andi Pratama` Group Manager dengan Position `Manager` dan Division `Operations`, `Sari Dewi` Group Role `Manage partner` dan `Manage allocation` tampil `2 roles`, `Dewi Lestari` Group Role `Manage active client`). Tabel Data Uji Dinamis TC tidak memuat data untuk spec ini.
- Akun kedua (ganti akun pada TC-AC-SG-287): Total Control entitas `Distributor Tiga Group` (Pre-setup #24, `Head Office` dengan anak `Floor 1` dan `Floor 2`, tanpa entitas) `totalControlTigaGroup_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.AC_SG_TIGA_PASSWORD`.
- Data tambahan (disediakan tim FE): daftar custom field aktif entitas Principal (nama tidak tertulis di Pre-setup; lihat Temuan untuk QA).
- Kemampuan teknis: Fixture BE (pembacaan state BE, seeding dan pemulihan data milik spec) dan sesi API aktor, disediakan tim FE/BE (lihat `suite.md`). Nilai data uji dirujuk lewat `Fixture.settingsGroup.<kunci>` (berkas `fixtures/settingsGroup.json` belum ada).
- Suite berjalan serial (`parallel: false`); spec ini tidak mengubah state global dan tidak menulis data.

## Test Steps

1. Ketik Search `Region A` pada toolbar tabel utama, tekan Enter
2. Klik angka Total User pada baris `Region A`

### TC-AC-SG-285: Screening Filter Panel popup Users

3. Klik ikon Filter pada toolbar popup
4. Verifikasi field Position dengan placeholder `All positions`
5. Verifikasi field Division dengan placeholder `All divisions`
6. Verifikasi field Group Role dengan placeholder `All group roles`
7. Verifikasi field Activation Status dengan placeholder `All statuses`
8. Verifikasi field Temporary User dengan placeholder `All`
9. Verifikasi field Temporary Until berupa date range dengan placeholder `Select date`
10. Verifikasi tampil satu field per custom field aktif
11. Verifikasi tombol `[Clear Field]` dan `[Apply]` tampil

### TC-AC-SG-286: Opsi filter Group Role: tier yang punya pemegang dan nama Group Role yang dipegang di node itu

12. Buka dropdown Group Role
13. Verifikasi opsi memuat `Total Control`, `Read Only`, dan `Group Manager` serta nama Group Role yang dipegang user di node ini: `Manage active client`, `Manage allocation`, dan `Manage partner`
14. Verifikasi opsi `Manage distributor` dan `Manage wallet & pricing` tidak muncul

### TC-AC-SG-288: Filter Group Role by tier Group Manager

15. Pilih `Group Manager` pada dropdown Group Role lalu klik `[Apply]`
16. Verifikasi tabel hanya menampilkan `Andi Pratama`
17. Verifikasi baris `Budi Santoso`, `Rina Wijaya`, `Sari Dewi`, dan `Dewi Lestari` tidak tampil pada tabel popup Users
18. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter

### TC-AC-SG-289: Filter Group Role by nama role individual menangkap user agregat "2 roles"

19. Pilih `Manage partner` pada dropdown Group Role lalu klik `[Apply]`
20. Verifikasi baris `Sari Dewi` tampil
21. Verifikasi kolom Group Role baris `Sari Dewi` berisi `2 roles` (filter mencocokkan keanggotaan role di baliknya, bukan string tampilan)
22. Klik `[Clear Field]` lalu klik `[Apply]` untuk membersihkan filter
23. Tutup popup lewat `[✕]`
24. Klik `(←)` pada kotak Search tabel utama untuk menutup input dan mereset tabel

### TC-AC-SG-287: Tier tanpa pemegang tidak ditawarkan sebagai opsi Group Role

25. Ganti akun: Logout, lalu login sebagai Total Control entitas `Distributor Tiga Group`
26. Buka halaman `Settings > Group` lewat sidebar
27. Klik angka Total User baris `Head Office`
28. Klik ikon Filter pada toolbar popup
29. Buka dropdown Group Role
30. Verifikasi opsi Group Role `Total Control` dan `Read Only` tampil
31. Verifikasi opsi `Group Manager` tidak muncul karena tidak ada pemegang di node ini
32. Verifikasi tidak ada nama Group Role individual karena tidak ada penugasan
33. Tutup popup lewat `[✕]`

## Notes

- Langkah penghubung (S-03): langkah 1 (Search untuk menemukan baris target `Region A`, R-16), pembersihan filter (`[Clear Field]` lalu `[Apply]`) di akhir TC-AC-SG-288 dan TC-AC-SG-289 (S-09), penutupan popup, klik `(←)` pada Search tabel utama, dan penutupan popup di akhir.
- Urutan TC dalam spec: 285, 286, 288, 289, 287. TC-AC-SG-287 memakai akun lain sehingga ditaruh sesudah Step ganti akun; bagian sesudah ganti akun tetap bermakna walau bagian sebelumnya gagal (bagian 3).
- Temuan untuk QA:
  - Perilaku panel Filter sesudah `[Apply]` di popup/modal tidak dinyatakan PRD; spec mengasumsikan panel tetap terbuka (pola spec 051 sampai 054 dan 070), sehingga klik ikon Filter berikutnya tidak diulang. Perlu konfirmasi FE.
  - TC-AC-SG-285 menyebut "satu field per custom field aktif" tanpa nama custom field entitas Principal; spec mengasersi keberadaan satu field per custom field aktif tanpa nama literal.
  - TC-AC-SG-287 menyebut "Total User baris `Head Office`" tanpa langkah Search; tree `Distributor Tiga Group` hanya berisi tiga group sehingga baris target terlihat tanpa Search.

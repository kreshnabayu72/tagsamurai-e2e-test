---
id: TC-FA-RP-E2E-189-detail-role-search-1
title: "Detail Role: Search (1/3)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-617
  - TC-FA-RP-618
coverage:
  web: automated
---

# Detail Role: Search (1/3)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris: 6 baris non-pola dan 35 baris pola Group Role. Baris non-pola: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata. Baris pola `Manage files` ada pada tujuh group Pre-setup #18 untuk lima user pola: Admin Utama (System Administrator, IT Operations), Siti Rahmawati (Finance Officer, Accounting & Tax), Rina Wulandari (`Operations Manager, Region 1`, `Asset Management "North"`), Dewi Anggraini (Internal Auditor, Internal Audit), Maya Anggraeni (Compliance Analyst, Legal); nama, Position, Division, dan email baris pola tidak memuat keyword uji di bawah) dan #18 (pohon group). Tidak diubah spec ini.
- Kolom uji Search TC-FA-RP-618:

| Kolom | Keyword | Hasil |
|---|---|---|
| Name | `ENDAH` | baris Endah Susanti tampil; tidak ada nama baris pola yang memuat `endah` |
| Group | `dock` | baris Fitri Handayani di `Dock 1` dan lima baris pola Group Role `Manage files` (Admin Utama, Siti Rahmawati, Rina Wulandari, Dewi Anggraini, Maya Anggraeni) di `Dock 1` tampil (enam baris); baris di group lain tidak tampil |
| Position | `warehouse` | baris Budi Santoso (Position `Warehouse Staff`) dan lima baris pola di `Logistics Warehouse` (cocok pada kolom Group `Logistics Warehouse`) tampil (enam baris); tidak ada baris pola yang Position-nya memuat `warehouse` |
| Division | `procure` | baris Endah Susanti tampil; Division baris pola tidak memuat `procure` |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-617: Siklus interaksi Search toolbar Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Arahkan kursor ke ikon Search di toolbar
5. Verifikasi tooltip `Search`
6. Klik ikon Search
7. Verifikasi kotak Search melebar
8. Verifikasi kursor otomatis fokus di input
9. Verifikasi placeholder input `Search name, position, division...`
10. Ketik `endah` tanpa menekan Enter
11. Verifikasi ikon `(✕)` muncul di dalam input
12. Verifikasi tabel belum tersaring (seluruh baris data tetap tampil, bukan hanya baris Endah Susanti)
13. Tekan Enter
14. Verifikasi tabel tersaring: hanya baris Endah Susanti
15. Klik ikon `(✕)` pada kotak Search
16. Verifikasi teks input terhapus
17. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus
18. Verifikasi tabel tetap menampilkan hasil pencarian terakhir (hanya baris Endah Susanti)
19. Tekan Enter pada input kosong
20. Verifikasi tabel kembali menampilkan seluruh data (baris selain Endah Susanti tampil kembali)
21. Ketik `endah` pada input, tekan Enter, lalu klik ikon `(←)`
22. Verifikasi kotak Search menutup
23. Verifikasi keyword dikosongkan
24. Verifikasi tabel langsung kembali ke seluruh data (baris selain Endah Susanti tampil kembali)

### TC-FA-RP-618: Search Detail Role per kelas teks: substring dan tidak case-sensitive

25. Untuk setiap baris tabel `Kolom uji Search TC-FA-RP-618` di Prerequisites, lakukan langkah 26 sampai 28
26. Ketik Search keyword pada baris iterasi, tekan Enter
27. Verifikasi hasil Search sesuai kolom Hasil pada baris iterasi (baris yang disebut pada kolom Hasil tampil dan baris lain tidak tampil)
28. Kosongkan isi kotak search, tekan Enter
29. Buka popup Setup Column lewat header `(⋯)` kolom Column Visibility lalu `Setup Column...`
30. Centang kolom `Email` lalu klik `[Save]`
31. Ketik Search `citralestari`, tekan Enter
32. Verifikasi kolom Email: hanya baris Citra Lestari yang tampil (email baris pola tidak memuat `citralestari`)
33. Kosongkan isi kotak search, tekan Enter
34. Sembunyikan kembali kolom `Email` lewat Setup Column lalu klik `[Save]` (pemulihan kolom bawaan)

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-617, 618). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 34.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 26 sampai 28 (4 iterasi).
- Spec ini di atas 35 langkah (34 langkah nominal, sekitar 43 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-617 langkah 8 menekan Enter pada input kosong setelah `(✕)`; spec mengasersi seluruh data (baris selain Endah Susanti tampil kembali) karena TC hanya menulis "seluruh data"; Pre-setup #39 kini 41 baris (6 non-pola dan 35 pola) sehingga jumlah tidak ditulis.

---
id: TC-FA-RP-E2E-206-table-user-picker-search-filter-dan-sort-1
title: "Table User Picker: Search, Filter, dan Sort (1/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-678
  - TC-FA-RP-679
coverage:
  web: automated
---

# Table User Picker: Search, Filter, dan Sort (1/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #41 (kandidat popup Assign Total Control, belum Total Control, 12 pengguna: Citra Lestari (HR Officer, HR), Dimas Pranata (IT Support, IT Operations; `TAG-2002`; `CC-100`; 10/01/26; `BN-77`), Endah Susanti (Procurement Officer, Procurement; `CC-200`; 15/02/26; `BN-88`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (Inactive), Gilang Prakoso (Pending Activation), Hana Permata (Temporary User Yes dengan Temporary Until terisi); email `[namalengkaptanpaspasi]@qwertysystem.net`), #36, #37, dan #17 (pengguna yang sudah Total Control, Read Only, dan variasi Home Group). Popup hanya dibaca; tidak ada Assign yang dikirim dan Pre-setup tidak diubah.
- Kolom uji Search TC-FA-RP-679:

| Kolom | Keyword | Hasil |
|---|---|---|
| Name | `ENDAH` | hanya Endah Susanti |
| Email | `gunawanhalim` | hanya Gunawan Halim |
| Position | `procure` | hanya Endah Susanti |
| Division | `it op` | hanya Dimas Pranata |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`).
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-678: Siklus interaksi Search toolbar Table User Picker

1. Klik Tab `Total Control`
2. Klik `[+ Assign]` pada Tab `Total Control` (popup Assign Total Control dengan Table User Picker)
3. Arahkan kursor ke ikon Search di toolbar
4. Verifikasi tooltip `Search`
5. Klik ikon Search
6. Verifikasi kotak Search melebar
7. Verifikasi kursor otomatis fokus di input
8. Verifikasi placeholder input `Search name, email, position...`
9. Ketik `endah` tanpa menekan Enter
10. Verifikasi ikon `(✕)` muncul di dalam input
11. Verifikasi tabel belum tersaring (baris kandidat selain Endah Susanti tetap tampil)
12. Tekan Enter
13. Verifikasi tabel tersaring: hanya Endah Susanti
14. Klik ikon `(✕)` pada kotak Search
15. Verifikasi teks input terhapus
16. Verifikasi kotak Search tetap terbuka dan kursor tetap fokus
17. Verifikasi tabel tetap menampilkan hasil pencarian terakhir (hanya Endah Susanti)
18. Tekan Enter pada input kosong
19. Verifikasi tabel kembali menampilkan seluruh data (daftar kandidat tanpa penyaringan)
20. Ketik `endah` pada input, tekan Enter, lalu klik ikon `(←)`
21. Verifikasi kotak Search menutup
22. Verifikasi keyword dikosongkan
23. Verifikasi tabel langsung kembali ke seluruh data (daftar kandidat tanpa penyaringan)

### TC-FA-RP-679: Search Table User Picker per kelas teks: substring dan tidak case-sensitive

24. Untuk setiap baris tabel `Kolom uji Search TC-FA-RP-679` di Prerequisites, lakukan langkah 25 sampai 27
25. Ketik Search keyword pada baris iterasi, tekan Enter
26. Verifikasi hasil Search sesuai kolom Hasil pada baris iterasi (hanya baris yang disebut tampil)
27. Kosongkan isi kotak search, tekan Enter
28. Tutup popup Assign Total Control dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-678, 679). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 28.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 25 sampai 27 (4 iterasi).
- Spec ini di atas 35 langkah (28 langkah nominal, sekitar 37 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:

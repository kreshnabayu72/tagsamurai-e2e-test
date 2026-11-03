---
id: TC-FA-RP-E2E-208-table-user-picker-search-filter-dan-sort-3
title: "Table User Picker: Search, Filter, dan Sort (3/5)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-684
  - TC-FA-RP-685
  - TC-FA-RP-686
  - TC-FA-RP-687
coverage:
  web: automated
---

# Table User Picker: Search, Filter, dan Sort (3/5)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #41 (kandidat popup Assign Total Control, belum Total Control, 12 pengguna: Citra Lestari (HR Officer, HR), Dimas Pranata (IT Support, IT Operations; `TAG-2002`; `CC-100`; 10/01/26; `BN-77`), Endah Susanti (Procurement Officer, Procurement; `CC-200`; 15/02/26; `BN-88`), Gunawan Halim, Hesti Rahma, Joko Santoso, Indra Kusuma, Dewi Anggraini, Maya Anggraeni, Yoga Pratama (Inactive), Gilang Prakoso (Pending Activation), Hana Permata (Temporary User Yes dengan Temporary Until terisi); email `[namalengkaptanpaspasi]@qwertysystem.net`), #36, #37, dan #17 (pengguna yang sudah Total Control, Read Only, dan variasi Home Group). Popup hanya dibaca; tidak ada Assign yang dikirim dan Pre-setup tidak diubah.
- Pre-setup #22 (Custom Field aktif `Cost Center`, `Joined Date`, `Badge No`) dipakai TC kolom Custom Field.
- Pilihan Filter TC-FA-RP-685:

| Field | Opsi | Hasil |
|---|---|---|
| Position | `Procurement Officer` | hanya Endah Susanti |
| Division | `IT Operations` | hanya Dimas Pranata |
| Status | `Inactive` | hanya Yoga Pratama |
| Activation Status | `Pending Activation` | hanya Gilang Prakoso |
| Temporary User | `Yes` | hanya Hana Permata |

- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hover pada ikon Search; membaca teks sel tabel; hapus preferensi kolom di browser (hook `after`). Memilih rentang tanggal pada date range picker.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-684: Screening Filter Panel Table User Picker

1. Klik Tab `Total Control`
2. Klik `[+ Assign]` pada Tab `Total Control` (popup Assign Total Control dengan Table User Picker)
3. Klik ikon Filter
4. Verifikasi Panel Filter popup memuat field `Position` (`All positions`), `Division` (`All divisions`), `Status` (`All statuses`), dan field curated `Activation Status`, `Temporary User`, `Temporary Until`, serta Custom Field aktif
5. Verifikasi footer panel memuat `[Clear Field]` dan `[Apply]`
6. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-685: Filter Table User Picker per kelas multi-select searchable

7. Klik ikon Filter
8. Untuk setiap baris tabel `Pilihan Filter TC-FA-RP-685` di Prerequisites, lakukan langkah 9 sampai 11
9. Pilih opsi pada baris iterasi di field baris iterasi, lalu klik `[Apply]`
10. Verifikasi hasil Filter sesuai kolom Hasil pada baris iterasi
11. Klik `[Clear Field]` lalu `[Apply]`
12. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-686: Filter Table User Picker per kelas date range

13. Klik ikon Filter
14. Pilih rentang tanggal field `Temporary Until` yang mencakup tanggal Temporary Until Hana Permata, lalu klik `[Apply]`
15. Verifikasi field Temporary Until: hanya Hana Permata yang tampil
16. Klik `[Clear Field]` lalu `[Apply]`
17. Tutup Filter Panel dengan klik ikon Filter

### TC-FA-RP-687: Isi opsi dropdown Filter Table User Picker diambil dari data tabel saat ini

18. Klik ikon Filter
19. Buka dropdown field `Position`
20. Verifikasi opsi Position memuat nilai kandidat yang ada pada daftar picker saat itu (`Procurement Officer`, `IT Support`, `HR Officer`)
21. Verifikasi opsi Position tidak memuat jabatan pengguna yang sudah Total Control (`Warehouse Staff`)
22. Tutup dropdown dengan Esc
23. Buka dropdown field `Division`
24. Verifikasi opsi Division memuat nilai kandidat yang ada pada daftar picker saat itu (`Procurement`, `IT Operations`, `HR`)
25. Tutup dropdown dengan Esc
26. Buka dropdown field `Status`
27. Verifikasi opsi Status: `Active`, `Inactive`
28. Tutup dropdown dengan Esc
29. Tutup Filter Panel dengan klik ikon Filter
30. Tutup popup Assign Total Control dengan Esc

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-684, 685, 686, 687). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 6, 12, 17, 22, 25, 28, 29, 30.
- Langkah berulang per baris tabel Prerequisites (parameter tiap iterasi ada di tabel; satu `Verifikasi` per klausa tetap): langkah 9 sampai 11 (5 iterasi).
- Spec ini di atas 35 langkah (30 langkah nominal, sekitar 42 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - Nilai Temporary Until Hana Permata tidak tertulis di Pre-setup #41 (hanya "terisi"); spec menunjuk nilai hasil seeding tanpa menuliskan tanggalnya.
  - TC-FA-RP-687 expected a menyebut contoh `Procurement Officer`, `IT Support`, `HR Officer` dan satu contoh tidak ada (`Warehouse Staff`); contoh nilai Division diturunkan dari Pre-setup #41 (Procurement, IT Operations, HR) karena TC tidak menyebut contoh Division.
  - TC-FA-RP-684 dan 685 memuat Custom Field aktif pada Panel Filter tetapi tidak merujuk Pre-setup #22 pada Precondition; spec memakai #22.
  - TC picker memulai dari Tab `Total Control` lalu `[+ Assign]` pada tiap TC; spec membuka popup sekali dan membersihkan state (Search, Filter, Sort, kolom) antar TC.

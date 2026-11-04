---
id: TC-FA-RP-E2E-204-detail-role-kombinasi-dan-state-halaman-1
title: "Detail Role: kombinasi dan state halaman (1/2)"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-FA-RP-671
  - TC-FA-RP-672
  - TC-FA-RP-673
  - TC-FA-RP-674
  - TC-FA-RP-675
coverage:
  web: automated
---

# Detail Role: kombinasi dan state halaman (1/2)

## Prerequisites

- Mode: FE+BE.
- Login di hook `before` spec ini sebagai Total Control (Pre-setup #2); halaman dibuka hook `beforeEach` suite (Fixed Asset > Settings > Role & Permission, Tab Total Control). Flag Guided Tooltip diatur hook suite (lihat `suite.md`).
- Akun aktor (password hanya lewat env):

| Role | Pre-setup | Email | Env var password |
|---|---|---|---|
| Total Control (Siti Rahmawati) | #2 | `totalControl_automated_{namaCompany}@qwertysystem.net` (`Fixture.fixedAssetRolePermission.akun.totalControl.email`) | `Spectra.env.FA_TC_PASSWORD` |

- Data Pre-setup (Company Alpha): #39 (Detail Role Group Role `Manage files`, 41 baris: 6 baris non-pola dan 35 baris pola Group Role. Baris non-pola: Ahmad Fauzi (Asset Custodian, Logistics) di `Data Center`; Budi Santoso (Warehouse Staff, Logistics) di `Helpdesk`; Citra Lestari (HR Officer, HR) di `Head Office`; Dimas Pranata (IT Support, IT Operations) di `Data Center`; Endah Susanti (Procurement Officer, Procurement) di `Rack A1`; Fitri Handayani (Finance Officer, Finance, Pending Email Confirmation, Temporary User Yes dengan Temporary Until terisi) di `Dock 1`; Detail Role Global Role `Manage Open API` dan `Manage accounting` terisi Ahmad Fauzi, Budi Santoso, Citra Lestari, Dimas Pranata. Baris pola `Manage files` ada pada tujuh group Pre-setup #18 untuk lima user pola: Admin Utama (System Administrator, IT Operations), Siti Rahmawati (Finance Officer, Accounting & Tax), Rina Wulandari (`Operations Manager, Region 1`, `Asset Management "North"`), Dewi Anggraini (Internal Auditor, Internal Audit), Maya Anggraeni (Compliance Analyst, Legal)) dan #18 (pohon group). Tidak diubah spec ini.
- Fixture `Fixture.fixedAssetRolePermission` belum ada; kunci akun, nama pengguna, group, dan nilai kolom yang diasersi ditambahkan tim FE.
- Kemampuan teknis (disediakan tim FE/BE): hapus preferensi kolom di browser (hook `after`); seret (drag and drop), hover, dan scroll horizontal pada tabel.
- Pemulihan: preferensi Setup Column tabel yang disimpan spec ini dihapus di hook `after` (hapus preferensi kolom di browser, bukan `[Reset to Default]`; kemampuan disediakan tim FE); Pre-setup bersama tidak diubah kecuali dinyatakan di atas. Pemulihan ini belum terdaftar di `suite.md` (lihat Temuan untuk QA).

## Test Steps

### TC-FA-RP-671: Kombinasi penuh Search, Filter, Sort, dan Pagination Detail Role

1. Klik Tab `System`
2. Klik Role Name `Manage files` pada section Group Role
3. Klik `All Groups` di Sidebar Group Tree
4. Ketik Search `Officer`, tekan Enter
5. Klik ikon Filter, pilih opsi `Finance Officer` dan `HR Officer` pada field `Position`, klik `[Apply]`
6. Klik header kolom Name dua kali (Name descending)
7. Ganti ukuran halaman menjadi 25
8. Verifikasi tabel menampilkan sembilan baris: tujuh baris pola Siti Rahmawati (Position `Finance Officer`; Pre-setup #39), Fitri Handayani, lalu Citra Lestari (irisan Search `Officer` dan Filter Position `Finance Officer` dan `HR Officer`, Sort Name descending)
9. Verifikasi ukuran halaman 25
10. Klik header kolom Name sekali (kembali ke default sort), ganti ukuran halaman menjadi 10, lalu lepas Filter dan Search (klik ikon Filter, `[Clear Field]`, `[Apply]`, tutup panel, klik `(←)` pada kotak Search)

### TC-FA-RP-672: Lepas Filter saat Search dan Sort aktif Detail Role

11. Ketik Search `Officer`, tekan Enter
12. Klik ikon Filter, pilih opsi `Finance Officer` dan `HR Officer` pada field `Position`, klik `[Apply]`
13. Klik header kolom Name dua kali (Name descending)
14. Klik `[Clear Field]` lalu `[Apply]`
15. Verifikasi tabel menampilkan sepuluh baris: tujuh baris pola Siti Rahmawati (Position `Finance Officer`; Pre-setup #39), Fitri Handayani, Endah Susanti, lalu Citra Lestari
16. Verifikasi keyword Search `Officer` tetap aktif menyaring tabel
17. Verifikasi Sort Name descending tetap aktif
18. Tutup Filter Panel, klik header kolom Name sekali (kembali ke default sort), lalu klik `(←)` pada kotak Search

### TC-FA-RP-673: Kosongkan Search saat Filter dan Sort aktif Detail Role

19. Ketik Search `Officer`, tekan Enter
20. Klik ikon Filter, pilih opsi `Finance Officer` dan `HR Officer` pada field `Position`, klik `[Apply]`
21. Klik header kolom Name dua kali (Name descending)
22. Kosongkan isi kotak search, tekan Enter
23. Verifikasi tabel menampilkan sembilan baris: tujuh baris pola Siti Rahmawati (Position `Finance Officer`; Pre-setup #39), Fitri Handayani, lalu Citra Lestari
24. Verifikasi kriteria Filter Position `Finance Officer` dan `HR Officer` tetap aktif menyaring tabel
25. Verifikasi Sort Name descending tetap aktif
26. Klik header kolom Name sekali (kembali ke default sort), lalu lepas Filter (klik ikon Filter, `[Clear Field]`, `[Apply]`, tutup panel)

### TC-FA-RP-674: Ganti kolom Sort saat Search dan Filter aktif Detail Role

27. Ketik Search `Officer`, tekan Enter
28. Klik ikon Filter, pilih opsi `Finance Officer` dan `HR Officer` pada field `Position`, klik `[Apply]`
29. Klik header kolom Division sekali (Division ascending)
30. Verifikasi Sort berpindah ke kolom Division ascending: tujuh baris pola Siti Rahmawati (`Accounting & Tax`; Pre-setup #39), Fitri Handayani (Finance), lalu Citra Lestari (HR)
31. Verifikasi Search `Officer` tidak direset
32. Verifikasi Filter Position tidak direset
33. Klik header kolom Division dua kali lagi (kembali ke default sort), lalu lepas Filter dan Search (klik ikon Filter, `[Clear Field]`, `[Apply]`, tutup panel, klik `(←)` pada kotak Search)

### TC-FA-RP-675: Pemulihan dari empty state Search dan Filter Detail Role

34. Klik ikon Filter, pilih opsi `Warehouse Staff` pada field `Position`, klik `[Apply]`
35. Ketik Search `Officer`, tekan Enter
36. Verifikasi kombinasi Filter Position `Warehouse Staff` dan Search `Officer` menampilkan `No results found`
37. Klik `[Clear Field]` lalu `[Apply]`
38. Verifikasi tabel pulih menampilkan Citra Lestari, Endah Susanti, Fitri Handayani, dan tujuh baris pola Siti Rahmawati (Position `Finance Officer`; Pre-setup #39)
39. Tutup Filter Panel dengan klik ikon Filter, lalu klik `(←)` pada kotak Search

## Notes

- Sumber TC: `tc-settings-role-permission.md` (TC-FA-RP-671, 672, 673, 674, 675). Seluruh TC berpost condition `-`; tidak ada asersi tambahan dari Post Condition.
- Langkah penghubung (tanpa awalan `Verifikasi`; dipakai untuk membuka konteks, menutup popup atau panel, membersihkan state, dan memulihkan kolom): langkah 1, 10, 18, 26, 33, 39.
- Spec ini di atas 35 langkah (39 langkah nominal, sekitar 39 langkah setelah ekspansi iterasi). Alasan: seluruh blok satu kelas fungsional pada satu tabel dengan data Pre-setup yang sama, tiap TC berdiri sendiri dan state-nya dibersihkan sebelum TC berikutnya, sehingga kegagalan satu blok tidak membuat blok lain kehilangan makna; langkah yang membengkak adalah iterasi per kolom atau per kata kunci yang parameternya ada di tabel Prerequisites.
- Temuan untuk QA:
  - TC-FA-RP-671 sampai 674 tidak menyebut cara memulihkan state antar TC; spec menulis langkah penghubung pemulihan (Search, Filter, Sort, ukuran halaman) sebelum TC berikutnya.
  - TC-FA-RP-671 mengganti ukuran halaman memakai hasil Search dan Filter sembilan baris (kurang dari ukuran halaman 25); kontrol pagination diasumsikan tampil untuk data kurang dari satu halaman. Urutan antar tujuh baris pola Siti Rahmawati (Name sama) tidak di-assert.

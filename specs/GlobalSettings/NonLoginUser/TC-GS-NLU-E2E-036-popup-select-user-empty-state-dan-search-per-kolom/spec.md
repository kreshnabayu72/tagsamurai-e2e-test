---
id: TC-GS-NLU-E2E-036-popup-select-user-empty-state-dan-search-per-kolom
title: "Popup Select User: empty state dan Search per kolom"
priority: High
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-111
  - TC-GS-NLU-112
  - TC-GS-NLU-113
coverage:
  web: automated
---

# Popup Select User: empty state dan Search per kolom

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (Dewi Anggraini Branch Manager Operations, Dewi Anggreni, Andi Wijaya `andi.wijaya@qwertysystem.net`, semua Active). Spec tidak membuat, mengubah, atau menghapus data backend.
- Data uji: kata kunci Search `zzzxxx`, `anggra`, `andi.w@`, `branch`, `OPERATIONS`, `Active`, `Dewi`.
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-111: Empty state Popup Select User saat pencarian tidak ditemukan

3. Ketik Search `zzzxxx`, tekan Enter
4. Verifikasi tabel menampilkan Illustration dengan Title `No results found` dan Description `Try adjusting your search or filter.`

### TC-GS-NLU-112: Search Popup Select User per kolom

5. Ganti isi kotak search dengan `anggra`, tekan Enter
6. Verifikasi baris Dewi Anggraini ditemukan (substring, case-insensitive) pada kolom Name
7. Ganti isi kotak search dengan `andi.w@`, tekan Enter
8. Verifikasi baris Andi Wijaya ditemukan pada kolom Email
9. Ganti isi kotak search dengan `branch`, tekan Enter
10. Verifikasi baris Dewi Anggraini (Branch Manager) ditemukan pada kolom Position
11. Ganti isi kotak search dengan `OPERATIONS`, tekan Enter
12. Verifikasi baris dengan Division Operations ditemukan walau huruf besar
13. Ganti isi kotak search dengan `Active`, tekan Enter
14. Verifikasi baris berstatus `Active` ditemukan (pencocokan exact atas teks `Active`)

### TC-GS-NLU-113: Siklus interaksi Search Popup Select User: reveal, clear, dan collapse

15. Klik `(←)` pada kotak Search sehingga kotak tertutup dan tabel kembali menampilkan seluruh baris
16. Klik icon Search
17. Verifikasi input melebar
18. Verifikasi kursor fokus di input
19. Verifikasi tooltip icon `Search`
20. Ketik `Dewi` tanpa menekan Enter
21. Verifikasi tabel belum tersaring (baris selain Dewi Anggraini dan Dewi Anggreni masih tampil)
22. Tekan Enter
23. Verifikasi tabel tersaring ke Dewi Anggraini dan Dewi Anggreni
24. Klik `(✕)` pada input
25. Verifikasi teks input terkosongkan
26. Verifikasi tabel belum reset dan masih tersaring ke Dewi Anggraini dan Dewi Anggreni
27. Tekan Enter pada input kosong
28. Verifikasi tabel reset dan menampilkan baris selain Dewi
29. Ketik `Dewi`, tekan Enter
30. Klik panah `(←)`
31. Verifikasi kotak search tertutup
32. Verifikasi keyword dikosongkan
33. Verifikasi tabel langsung reset dan menampilkan baris selain Dewi
34. Klik `[Cancel]`
35. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung tanpa `Verifikasi`: langkah 15 (menutup kotak Search yang masih berisi `Active` sebelum TC-GS-NLU-113 menguji siklus input dari keadaan tertutup) dan langkah 34 sampai 35 (menutup popup; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- Total 35 langkah, tepat di batas sekitar 35.
- Temuan untuk QA: tidak ada.

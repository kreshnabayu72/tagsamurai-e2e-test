---
id: TC-GS-NLU-E2E-041-popup-select-user-aksesibilitas-grid-keyboard-focus-trap
title: "Popup Select User: aksesibilitas grid, keyboard, focus trap"
priority: Medium
caseType: Positive
status: draft
sourceTc:
  - TC-GS-NLU-131
  - TC-GS-NLU-132
  - TC-GS-NLU-133
coverage:
  web: automated
---

# Popup Select User: aksesibilitas grid, keyboard, focus trap

## Prerequisites

- Mode: FE+BE.
- Akun aktor: Total Control (Siti Nurhaliza) `totalControlGlobalSettings_automated_{namaCompany}@qwertysystem.net`, password `Spectra.env.GS_TC_PASSWORD`. Login di hook `before` spec ini; halaman dibuka hook `beforeEach` suite; hook `after` mengembalikan sesi ke akun default suite (Total Control). Password tidak ditulis di spec atau fixture.
- Guided Tooltip: mengikuti pernyataan Guided Tooltip di hook suite pada `suite.md`; spec ini tidak mengatur flag sendiri.
- Fixture: nilai data uji dirujuk lewat `fixtures/nonLoginUser.json` (fixture belum ada; dibuat pada tahap script).
- Data Pre-setup (hanya dibaca, Tabel Data Uji Pre-setup No. 9 sampai 13): pool Login User Represented By No. 10 (Active; Dewi Anggraini berada di halaman pertama, urutan Name A-Z). Spec tidak membuat, mengubah, atau menghapus data backend; Popup Create tidak pernah di-Submit.
- Asersi hanya atribut dan fokus pada DOM (tanpa screen reader).
- State global: tidak ada yang diubah.

## Test Steps

1. Klik `[+ Non-Login User]` sehingga Popup Create Non-Login User terbuka
2. Klik `[+ Select User]` pada field Represented By sehingga Popup Select User terbuka

### TC-GS-NLU-131: Accessibility Popup Select User: semantik grid dan penanda baris terpilih

3. Verifikasi tabel `role="grid"` dengan `aria-multiselectable="false"`
4. Verifikasi baris data `role="row"` dengan `aria-selected="false"`
5. Klik baris Dewi Anggraini
6. Verifikasi baris Dewi Anggraini `aria-selected="true"`
7. Verifikasi baris lain `aria-selected="false"`
8. Verifikasi baris terpilih punya penanda non-warna (tanda centang di sel Name) selain sorotan warna

### TC-GS-NLU-132: Accessibility Popup Select User: navigasi keyboard memilih baris

9. Klik `[Cancel]` lalu klik `[+ Select User]` sehingga Popup Select User terbuka tanpa baris terpilih
10. Tekan Tab hingga fokus masuk baris tabel
11. Tekan `↓` dua kali
12. Verifikasi fokus berpindah antar baris dengan `↓`
13. Verifikasi tidak ada baris yang terpilih (`aria-selected="true"`)
14. Tekan `Enter`
15. Verifikasi `Enter` memilih baris yang fokus
16. Tekan `↑`
17. Tekan `Space`
18. Verifikasi `Space` memilih baris yang fokus
19. Verifikasi pilihan berpindah dari baris sebelumnya

### TC-GS-NLU-133: Accessibility Popup Select User: urutan fokus, focus trap, Esc, dan pengumuman error

20. Klik `[Cancel]` lalu klik `[+ Select User]` sehingga Popup Select User terbuka tanpa baris terpilih
21. Verifikasi fokus awal di kolom Search
22. Tekan Tab berulang
23. Verifikasi urutan Tab: Filter, baris tabel, pagination, `[Cancel]`, `[Select]`
24. Verifikasi fokus ter-trap di dalam popup
25. Klik `[Select]` tanpa pilihan
26. Verifikasi error `You must pick a user` diumumkan lewat `role="alert"`
27. Verifikasi fokus tetap di `[Select]`
28. Tekan `Esc`
29. Verifikasi `Esc` menutup popup tanpa memilih
30. Klik `✕` pada Popup Create Non-Login User

## Notes

- Mode: FE+BE. Sumber: `global-settings/non-login-user/TestCases/tc-non-login-user.md`. Subjudul `###` memetakan langkah ke id TC granular. Urutan TC sumber dipertahankan.
- Langkah penghubung tanpa `Verifikasi`: langkah 9 dan 20 (menutup dan membuka ulang popup supaya tiap TC mulai tanpa baris terpilih; pilihan Dewi Anggraini dari TC-GS-NLU-131 dan pilihan dari TC-GS-NLU-132 dibuang oleh `[Cancel]`) dan langkah 30 (menutup Popup Create; Represented By tidak dipilih sehingga tanpa dialog Unsaved Changes).
- Temuan untuk QA:
  - TC-GS-NLU-132 langkah 3 sampai 6 tidak menyebut baris yang menjadi sasaran `↓`, `Enter`, dan `Space`; spec mengasersi hanya perilaku pemilihan dan perpindahan pilihan, bukan nama baris tertentu.
  - TC-GS-NLU-133 Expected butir b ("Fokus ter-trap di dalam popup") tidak menyebut jumlah penekanan Tab; spec memakai penekanan Tab berulang melewati `[Select]`.
